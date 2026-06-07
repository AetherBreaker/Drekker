# Standard library imports
from typing import Literal

# First party imports
from drekker.sheets.entry_types import EntryType
from drekker.sheets.entry_types.attrbase import AttrEntryBase
from drekker.typing.enums import SkillName


class SkillEntry(AttrEntryBase):
  type: Literal[EntryType.SKILL]
  name: SkillName
