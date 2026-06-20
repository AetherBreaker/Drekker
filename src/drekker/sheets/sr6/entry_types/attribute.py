# Standard library imports
from typing import Literal

# First party imports
from drekker.enumerated_constants.character_values import AttributeName
from drekker.sheets.base.types import EntryTypeBase
from drekker.sheets.sr6.entry_types.attrbase import AttrEntryBase


class AttributeEntry(AttrEntryBase[]):
  type: Literal[EntryTypeBase.ATTRIBUTE]
  name: AttributeName
