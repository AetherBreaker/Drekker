# Standard library imports
from functools import cached_property
from typing import cast

# First party imports
from drekker.sheets.base import EntryBase, EntryTypeBase
from drekker.sheets.base.types import Costs, TargetCodeBase


class AttrEntryBase[TargetCode_T: TargetCodeBase, EntryTypeT: EntryTypeBase, Cost_T: Costs](
  EntryBase[TargetCode_T, EntryTypeT, Cost_T]
):
  @cached_property
  def costs(self) -> Cost_T:
    args = self.__pydantic_generic_metadata__["args"]
    if args:
      cost_cls = cast("type[Cost_T]", args[2])
    else:
      raise TypeError("Cost type parameter is required for AttrEntryBase")
    return cost_cls(KARMA=self.rating * 5)

  @cached_property
  def rating(self) -> int:
    count = 0
    for entry in self._top.entry_stack:
      if entry is self:
        break
      if isinstance(entry, type(self)):
        count += 1
    return count
