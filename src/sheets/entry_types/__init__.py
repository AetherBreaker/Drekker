from abc import ABC, abstractmethod
from collections.abc import Callable
from decimal import Decimal
from enum import StrEnum, auto
from functools import cached_property
from typing import TYPE_CHECKING, Annotated, NamedTuple

from drek_typing.enums import CharacterValue
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
  SKILL_LANGUAGE = auto()
  SKILL_KNOWLEDGE = auto()
  SKILL_SPECIALIZATION = auto()
  SKILL_EXPERTISE = auto()
  QUALITY = auto()
  GEAR = auto()


class CostType(StrEnum):
  KARMA = auto()
  NUYEN = auto()
  ESSENCE = auto()


class Costs(NamedTuple):
  KARMA: int = 0
  NUYEN: int = 0
  ESSENCE: Decimal = Decimal(0)


class EntryBase[EntryTypeT: EntryType, NameT: str](ABC, ConfiguredBaseModel):
  type: EntryTypeT
  name: NameT
  modifications: Annotated[tuple[ModificationEntry, ...], Field(default_factory=tuple)]

  @cached_property
  @abstractmethod
  def costs(self) -> Costs:
    raise NotImplementedError("Subclasses must implement costs property")

  @cached_property
  @abstractmethod
  def rating(self) -> int | Decimal:
    raise NotImplementedError("Subclasses must implement rating property")
