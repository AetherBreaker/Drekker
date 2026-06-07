# Standard library imports
from typing import Literal
from typing.enums import SkillName

# First party imports
from drekker.sheets.entry_types.attrbase import AttrEntryBase
from sheets.entry_types import EntryType


class SkillEntry(AttrEntryBase):
  type: Literal[EntryType.SKILL]
  name: SkillName
