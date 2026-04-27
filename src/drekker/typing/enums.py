from enum import StrEnum, auto


class AttributeName(StrEnum):
  BODY = auto()
  AGILITY = auto()
  REACTION = auto()
  STRENGTH = auto()
  CHARISMA = auto()
  INTUITION = auto()
  LOGIC = auto()
  WILLPOWER = auto()

  @staticmethod
  def _generate_next_value_(name, start, count, last_values) -> str:
    """
    Return the title-cased version of the member name.
    """
    return name.title()
