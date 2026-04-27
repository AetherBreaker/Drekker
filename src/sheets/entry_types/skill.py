from typing import Literal

from drek.typing.enums import SkillName

from sheets.entry_types import EntryType
from sheets.entry_types.attrbase import AttrEntryBase


class SkillEntry(AttrEntryBase):
  type: Literal[EntryType.SKILL]
  name: SkillName
