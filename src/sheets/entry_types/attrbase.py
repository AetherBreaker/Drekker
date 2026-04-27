from functools import cached_property

from sheets.entry_types import EntryBase


class AttrEntryBase(EntryBase):
  @cached_property
  def cost(self) -> int:
    return self._count_attr_entries_until_self * 5

  @cached_property
  def _count_attr_entries_until_self(self) -> int:
    count = 0
    for entry in self._top.entry_stack:
      if entry is self:
        break
      if isinstance(entry, type(self)):
        count += 1
    return count
