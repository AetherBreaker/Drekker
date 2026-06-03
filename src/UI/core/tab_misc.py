from textual.widgets import Static

from ui.core.core_base import CoreTabContainerBase
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from textual.widget import Widget
  from textual.app import ComposeResult


class MiscTab(CoreTabContainerBase):
  """Identity information, notes, and miscellaneous tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      "Miscellaneous",
      *children,
      name="miscellaneous",
      id="miscellaneous",
      disabled=disabled,
    )

  def compose(self) -> ComposeResult:
    yield Static("[Miscellaneous — coming soon]")
