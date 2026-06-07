# Standard library imports
from enum import auto

# First party imports
from drekker.typing.enums import StrEnumBase


class NoteTarget(StrEnumBase):
  """Enumeration of possible target locations to send notes to in the UI."""

  PLACEHOLDER = auto()
