from typing import Literal
from typing.enums import AttributeName

from sheets.entry_types import EntryType
from sheets.entry_types.attrbase import AttrEntryBase


class AttributeEntry(AttrEntryBase):
  type: Literal[EntryType.ATTRIBUTE]
  name: AttributeName
