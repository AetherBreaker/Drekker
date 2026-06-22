# Standard library imports
from enum import auto

# First party imports
from drekker.typing import StrEnumBase


class CharacterValue(StrEnumBase):
  """Base class for typing fields that accept a value of one of it's subclasses."""


class AttributeName(CharacterValue):
  BODY = auto()
  AGILITY = auto()
  REACTION = auto()
  STRENGTH = auto()
  CHARISMA = auto()
  INTUITION = auto()
  LOGIC = auto()
  WILLPOWER = auto()


class SkillName(CharacterValue):
  ASTRAL = auto()
  ATHLETICS = auto()
  BIOTECH = auto()
  CLOSE_COMBAT = auto()
  CON = auto()
  CONJURING = auto()
  CRACKING = auto()
  ELECTRONICS = auto()
  ENCHANTING = auto()
  ENGINEERING = auto()
  EXOTIC_WEAPONS = auto()
  FIREARMS = auto()
  INFLUENCE = auto()
  OUTDOORS = auto()
  PERCEPTION = auto()
  PILOTING = auto()
  SORCERY = auto()
  STEALTH = auto()
  TASKING = auto()
