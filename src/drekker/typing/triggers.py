# Standard library imports
from enum import auto

# First party imports
from drekker.typing.enums import StrEnumBase


class Triggers(StrEnumBase):
  """Enum for triggers that can be used in the datapack."""

  ON_LOGIC_TEST = auto()
  APPEARANCE = auto()
