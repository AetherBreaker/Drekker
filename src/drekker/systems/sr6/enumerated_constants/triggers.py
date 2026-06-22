# Standard library imports
from enum import auto

# First party imports
from drekker.typing import StrEnumBase


class Triggers(StrEnumBase):
  """Enum for triggers that can be used in the datapack."""

  ON_LOGIC_TEST = auto(), "Actions linked to this trigger are performed when a logic test is made."
