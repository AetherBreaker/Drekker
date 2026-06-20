# Standard library imports
from typing import Literal

# First party imports
from drekker.enumerated_constants.character_values import SkillName
from drekker.sheets.base.types import EntryTypeBase
from drekker.sheets.sr6.entry_types.attrbase import AttrEntryBase


class SkillEntry(AttrEntryBase):
  type: Literal[EntryTypeBase.SKILL]
  name: SkillName
