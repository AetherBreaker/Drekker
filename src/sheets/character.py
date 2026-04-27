from collections.abc import Callable
from decimal import Decimal
from enum import StrEnum, auto
from logging import getLogger
from typing import Annotated

from pydantic import BaseModel, Field, RootModel
from sheets import ConfiguredBaseModel

logger = getLogger(__name__)


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


type Complex = str
type ComplexPrebuilt = Callable[[SR6Character], int | Decimal]


class ChoiceType(StrEnum):
  ATTRIBUTE = auto()
  SKILL = auto()
  QUALITY = auto()
  GEAR = auto()
  ...


class ModificationEntry(BaseModel):
  type: ModType
  value: int | Decimal | Complex


class BaseChoiceEntry(ConfiguredBaseModel):
  type: ChoiceType
  name: str
  costs: dict[str, int | Decimal] = Field(default_factory=dict)
  modifications: dict[ModTarget, ModificationEntry] = Field(default_factory=dict)


class SR6Character(ConfiguredBaseModel):
  choice_stack: list[BaseChoiceEntry] = Field(default_factory=list)
