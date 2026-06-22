# Standard library imports
from decimal import Decimal
from enum import auto
from typing import NamedTuple

# First party imports
from drekker.typing import StrEnumBase

__all__ = ["Costs", "EntryTypeBase", "ModType", "TargetCodeBase"]


class ModType(StrEnumBase):
  NUMERIC = auto()

  # Used for things that the sheet class will by default check for
  ENABLE = auto()
  DISABLE = auto()

  # Used for things that want to toggle the existing state of a feature rather than
  # override it
  TOGGLE = auto()


class Costs(NamedTuple):
  KARMA: int = 0
  NUYEN: int = 0
  ESSENCE: Decimal = Decimal(0)


class TargetCodeBase(StrEnumBase):
  # STRENGTH = auto()
  # BODY = auto()
  ...


class EntryTypeBase(StrEnumBase):
  # ATTRIBUTE = auto()
  # SKILL = auto()
  # SKILL_LANGUAGE = auto()
  # SKILL_KNOWLEDGE = auto()
  # SKILL_SPECIALIZATION = auto()
  # SKILL_EXPERTISE = auto()
  # QUALITY = auto()
  # GEAR = auto()
  ...
