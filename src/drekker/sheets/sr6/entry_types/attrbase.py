# Standard library imports
from functools import cached_property

# First party imports
from drekker.sheets.base import EntryBase
from drekker.sheets.base.types import Costs


class AttrEntryBase(EntryBase):
  @cached_property
  def costs(self) -> Costs:
    return Costs(KARMA=self.rating * 5)

  @cached_property
  def rating(self) -> int:
    count = 0
    for entry in self._top.entry_stack:
      if entry is self:
        break
      if isinstance(entry, type(self)):
        count += 1
    return count
