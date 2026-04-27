from collections.abc import Callable
from decimal import Decimal
from enum import StrEnum, auto
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from sheets import ConfiguredBaseModel

if TYPE_CHECKING:
  from sheets.sr6character import SR6Character

type Complex = str
type ComplexPrebuilt = Callable[["SR6Character"], int | Decimal]


class ModTarget(StrEnum):
  ATTRIBUTE = auto()
  SKILL = auto()
  ESSENCE = auto()
  KARMA = auto()
  NUYEN = auto()
  REPUTATION = auto()
  HEAT = auto()
  ...


class ModType(StrEnum):
  ADD = auto()
  SUBTRACT = auto()
  MULTIPLY = auto()
  DIVIDE = auto()
  FLOOR_DIVIDE = auto()
  MODULO = auto()
  COMPLEX_PREBUILT = auto()
  COMPLEX = auto()  # TODO for custom formulas. Must be a simple python lambda that accepts an instance of SR6Character
  # TODO and returns a number.
  ...


class ModificationEntry(ConfiguredBaseModel):
  target: ModTarget
  type: ModType
  value: int | Decimal | Complex


class EntryType(StrEnum):
  ATTRIBUTE = auto()
  SKILL = auto()
  QUALITY = auto()
  GEAR = auto()
  ...


class EntryBase[EntryTypeT: EntryType, NameT: str](ConfiguredBaseModel):
  type: EntryTypeT
  name: NameT
  costs: Annotated[dict[str, int | Decimal], Field(default_factory=dict)]
  modifications: Annotated[tuple[ModificationEntry, ...], Field(default_factory=tuple)]
