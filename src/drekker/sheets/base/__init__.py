# pyright: reportImportCycles=false
# Standard library imports
from abc import ABC
from collections.abc import Callable
from decimal import Decimal
from functools import cached_property, wraps
from logging import getLogger
from typing import Annotated, Any, Self, cast, override

# Third party imports
from pydantic import Field, model_validator

# First party imports
from drekker.enumerated_constants.character_values import CharacterValue
from drekker.sheets.base._sheet_basemodels import ConfiguredBaseModel, ConfiguredListModel
from drekker.sheets.base.types import Costs, EntryTypeBase, ModType, TargetCodeBase

logger = getLogger(__name__)


def default_criteria(stack: EntryStack) -> bool:
  return any(stack.mods_updated.values()) or any(stack.entries_updated.values())


def cache_if[**TP, TR](
  re_calc_criteria: Callable[[EntryStack], bool] = default_criteria,
) -> Callable[[Callable[TP, TR]], Callable[TP, TR]]:
  """A decorator that recalculates the functions return value if the re_calc_criteria function returns True
  Otherwise it returns the cached value for the given arguements."""
  cache = {}
  sep = object()

  def _decorator(func: Callable[TP, TR]) -> Callable[TP, TR]:
    @wraps(func)
    def _wrapper(*args: TP.args, **kwargs: TP.kwargs) -> TR:
      self = cast("SheetBase", args[0])
      cache_key = (*args[1:], sep, *tuple(sorted(kwargs.items())))
      if cache_key not in cache or re_calc_criteria(self.entry_stack):
        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result
      else:
        return cache[cache_key]

    return _wrapper

  return _decorator


class Modification[TargetCode_T: TargetCodeBase](ConfiguredBaseModel):
  target: CharacterValue
  type: ModType
  op: Callable[[SheetBase], dict[TargetCode_T, int | Decimal | bool]]

  # Stored here to calculate a hash of the op inputs
  _op_input_hash: int
  _op_cached_result: dict[TargetCode_T, int | Decimal | bool]

  @property
  def value(self) -> dict[TargetCode_T, int | Decimal | bool]:
    top_hash = hash(self._top)
    if self._op_input_hash != top_hash:
      self._op_cached_result = self.op(self._top)
      self._op_input_hash = top_hash
    return self._op_cached_result

  @override
  def _post_init(self) -> None:
    # calculate the initial hash of the op input, which should always be self._top
    self._op_input_hash = hash(self._top)

  def __call__(self) -> dict[TargetCode_T, int | Decimal | bool]:
    return self.value


class EntryBase[TargetCode_T: TargetCodeBase, EntryTypeT: EntryTypeBase](ABC, ConfiguredBaseModel):
  type: EntryTypeT
  name: str
  modifications: Annotated[tuple[Modification[TargetCode_T], ...], Field(default_factory=tuple)]

  @cached_property
  def costs(self) -> Costs: ...

  @cached_property
  def rating(self) -> int | Decimal: ...


class EntryStackRoot[TargetCode_T: TargetCodeBase, EntryTypeT: EntryTypeBase](
  ConfiguredListModel[EntryBase[TargetCode_T, EntryTypeT]]
): ...


class EntryStack[TargetCode_T: TargetCodeBase, EntryTypeT: EntryTypeBase](ConfiguredBaseModel):
  """A wrapper around a list of EntryBase objects that represents the stack of entries on a character sheet."""

  stack: EntryStackRoot[TargetCode_T, EntryTypeT] = Field(default_factory=lambda: EntryStackRoot[TargetCode_T, EntryTypeT](root=[]))

  mods_updated: dict[TargetCode_T, bool] = Field(default_factory=dict, exclude=True)
  entries_updated: dict[EntryTypeT, bool] = Field(default_factory=dict, exclude=True)

  @model_validator(mode="after")
  def _populate_updated_dicts(self) -> Self:
    """Seed the tracking dicts with a key for every member of the concrete enum bound to each
    type parameter, defaulting every value to False."""
    args = self.__pydantic_generic_metadata__["args"]
    if args:
      target_code_cls, entry_type_cls = cast("tuple[type[TargetCodeBase], type[EntryTypeBase]]", args)
    else:
      target_code_cls, entry_type_cls = TargetCodeBase, EntryTypeBase
    if not self.mods_updated:
      self.mods_updated = cast("dict[TargetCode_T, bool]", dict.fromkeys(target_code_cls, False))
    if not self.entries_updated:
      self.entries_updated = cast("dict[EntryTypeT, bool]", dict.fromkeys(entry_type_cls, False))
    return self


class SheetBase(ConfiguredBaseModel):
  entry_stack: Annotated[EntryStack, Field(default_factory=list)]

  def get_filtered_stack(self, criteria: type[EntryBase]) -> list[EntryBase]:
    return [entry for entry in self.entry_stack if isinstance(entry, criteria)]

  @property
  @cache_if()
  def modification_stack(self) -> tuple[Modification, ...]:  # Read only
    return tuple(mod for entry in self.entry_stack.stack for mod in entry.modifications)

  @override
  def model_post_init(self, _: Any) -> None:
    if self._top is None:  # pyright: ignore[reportUnnecessaryComparison]
      self._top = self
      self._propogate_top()

  @override
  def __hash__(self) -> int:
    # serialize self to a json string and return it's hash
    return hash(self.model_dump_json())
