from enum import StrEnum, auto


class StrEnumBase(StrEnum):
  @staticmethod
  def _generate_next_value_(name, start, count, last_values) -> str:
    """
    Return the title-cased version of the member name.
    """
    return name.title()


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
