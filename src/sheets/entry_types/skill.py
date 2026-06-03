from typing import Literal, TYPE_CHECKING


from sheets.entry_types.attrbase import AttrEntryBase

if TYPE_CHECKING:
  from drek_typing.enums import SkillName
  from sheets.entry_types import EntryType


class SkillEntry(AttrEntryBase):
  type: Literal[EntryType.SKILL]
  name: SkillName
