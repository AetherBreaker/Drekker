from typing import Literal, TYPE_CHECKING


from sheets.entry_types.attrbase import AttrEntryBase

if TYPE_CHECKING:
  from sheets.entry_types import EntryType
  from drek_typing.enums import AttributeName


class AttributeEntry(AttrEntryBase):
  type: Literal[EntryType.ATTRIBUTE]
  name: AttributeName
