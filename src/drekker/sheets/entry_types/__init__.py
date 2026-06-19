# Standard library imports
from abc import ABC
from collections.abc import Callable
from decimal import Decimal
from enum import StrEnum, auto
from functools import cached_property
from typing import TYPE_CHECKING, Annotated, NamedTuple, override

# Third party imports
from pydantic import Field

# First party imports
from drekker.enumerated_constants.character_values import CharacterValue
from drekker.sheets import ConfiguredBaseModel

if TYPE_CHECKING:
  # First party imports
  from drekker.sheets.sr6character import SR6Character


class ModTargetType(StrEnum):
  ATTRIBUTE = auto()
  SKILL = auto()
  ESSENCE = auto()
  KARMA = auto()
  NUYEN = auto()
  REPUTATION = auto()
  HEAT = auto()


class ModType(StrEnum):
  NUMERIC = auto()

  # Used for things that the sheet class will by default check for
  ENABLE = auto()
  DISABLE = auto()

  # Used for things that want to toggle the existing state of a feature rather than
  # override it
  TOGGLE = auto()


ENABLE_SENTINEL = object()
DISABLE_SENTINEL = object()
TOGGLE_SENTINEL = object()

type Sentinel = object


class ModificationEntry[OpR_T: int | Decimal | bool | Sentinel](ConfiguredBaseModel):
  target: CharacterValue
  target_type: ModTargetType
  type: ModType
  op: Callable[["SR6Character"], OpR_T]

  # Stored here to calculate a hash of the op inputs
  _op_input_hash: int
  _op_cached_result: OpR_T

  @property
  def value(self) -> OpR_T:
    if self._op_input_hash != hash(self._top):
      return self.op(self._top)
    return self._op_cached_result

  @override
  def _post_init(self) -> None:
    # calculate the initial hash of the op input, which should always be self._top
    self._op_input_hash = hash(self._top)


class EntryType(StrEnum):
  ATTRIBUTE = auto()
  SKILL = auto()
  SKILL_LANGUAGE = auto()
  SKILL_KNOWLEDGE = auto()
  SKILL_SPECIALIZATION = auto()
  SKILL_EXPERTISE = auto()
  QUALITY = auto()
  GEAR = auto()


class Costs(NamedTuple):
  KARMA: int = 0
  NUYEN: int = 0
  ESSENCE: Decimal = Decimal(0)


class EntryBase[EntryTypeT: EntryType, NameT: str](ABC, ConfiguredBaseModel):
  type: EntryTypeT
  name: NameT
  modifications: Annotated[tuple[ModificationEntry, ...], Field(default_factory=tuple)]

  @cached_property
  def costs(self) -> Costs: ...

  @cached_property
  def rating(self) -> int | Decimal: ...
