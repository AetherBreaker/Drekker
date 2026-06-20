# Standard library imports
from decimal import Decimal
from enum import StrEnum, auto
from typing import NamedTuple


class Costs(NamedTuple):
  KARMA: int = 0
  NUYEN: int = 0
  ESSENCE: Decimal = Decimal(0)


class ModType(StrEnum):
  NUMERIC = auto()

  # Used for things that the sheet class will by default check for
  ENABLE = auto()
  DISABLE = auto()

  # Used for things that want to toggle the existing state of a feature rather than
  # override it
  TOGGLE = auto()


class TargetCodeBase(StrEnum):
  # STRENGTH = auto()
  # BODY = auto()
  ...


class EntryTypeBase(StrEnum):
  # ATTRIBUTE = auto()
  # SKILL = auto()
  # SKILL_LANGUAGE = auto()
  # SKILL_KNOWLEDGE = auto()
  # SKILL_SPECIALIZATION = auto()
  # SKILL_EXPERTISE = auto()
  # QUALITY = auto()
  # GEAR = auto()
  ...
