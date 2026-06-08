# Standard library imports
from enum import auto

# First party imports
from drekker.typing import StrEnumBase


class NoteTarget(StrEnumBase):
  """Enumeration of possible target locations to send notes to in the UI."""

  APPEARANCE = auto(), "Sends note to the appearance section of the character sheet."
  ALL_ROLLS = auto(), "Sends note to all rolls section of the character sheet."


class ModificationTarget(StrEnumBase):
  """Enumeration of possible target locations to send modifications to in the UI."""

  CONTACTS_RATING = auto(), "Used when making modifications to contact ratings."
  CONTACTS_LOYALTY = auto(), "Used when making modifications to contact loyalty."
