# Standard library imports
from typing import Literal

# First party imports
from drekker.enumerated_constants.character_values import SkillName
from drekker.sheets.entry_types import EntryType
from drekker.sheets.entry_types.attrbase import AttrEntryBase


class SkillEntry(AttrEntryBase):
  type: Literal[EntryType.SKILL]
  name: SkillName
