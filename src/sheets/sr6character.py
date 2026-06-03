from enum import StrEnum
from functools import wraps
from logging import getLogger
from typing import Annotated, Any, cast, TYPE_CHECKING

from pydantic import Field

from sheets import ConfiguredBaseModel, ConfiguredListModel
from sheets.entry_types import EntryBase, EntryType, ModificationEntry, ModTargetType

if TYPE_CHECKING:
  from collections.abc import Callable

logger = getLogger(__name__)


def _new_updated_dict[KeyT: StrEnum](keytype: type[KeyT]) -> Callable[[], dict[KeyT, bool]]:
  def _new_dict() -> dict[KeyT, bool]:
    return dict.fromkeys(keytype, False)

  return _new_dict


def default_criteria(stack: EntryStack) -> bool:
  return any(stack._mods_updated.values()) or any(stack._entries_updated.values())


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
      self = cast("SR6Character", args[0])
      cache_key = (*args[1:], sep, *tuple(sorted(kwargs.items())))
      if cache_key not in cache or re_calc_criteria(self.entry_stack):
        result = func(*args, **kwargs)
        cache[cache_key] = result
        return result
      else:
        return cache[cache_key]

    return _wrapper

  return _decorator


class EntryStack(ConfiguredListModel[EntryBase]):
  """A wrapper around a list of EntryBase objects that represents the stack of entries on a character sheet."""

  _mods_updated: dict[ModTargetType, bool] = Field(default_factory=_new_updated_dict(ModTargetType), exclude=True)
  _entries_updated: dict[EntryType, bool] = Field(default_factory=_new_updated_dict(EntryType), exclude=True)


class SR6Character(ConfiguredBaseModel):
  entry_stack: Annotated[EntryStack, Field(default_factory=list)]

  def get_filtered_stack(self, criteria: type[EntryBase]) -> list[EntryBase]:
    return [entry for entry in self.entry_stack if isinstance(entry, criteria)]

  @property
  @cache_if()
  def modification_stack(self) -> tuple[ModificationEntry, ...]:  # Read only
    return tuple(mod for entry in self.entry_stack for mod in entry.modifications)

  def model_post_init(self, _: Any) -> None:
    if self._top is None:
      self._top = self
      self._propogate_top()

  def __hash__(self) -> int:
    # serialize self to a json string and return it's hash
    return hash(self.model_dump_json())
