# Standard library imports
from typing import Literal

# First party imports
from drekker.sheets.entry_types import EntryType
from drekker.sheets.entry_types.attrbase import AttrEntryBase
from drekker.typing.enums import AttributeName


class AttributeEntry(AttrEntryBase):
  type: Literal[EntryType.ATTRIBUTE]
  name: AttributeName
