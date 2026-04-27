from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static

from ui.core.core_base import CoreTabContainerBase


class MiscTab(CoreTabContainerBase):
  """Identity information, notes, and miscellaneous tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      title="Miscellaneous",
      *children,
      name="miscellaneous",
      id="miscellaneous",
      disabled=disabled,
    )

  def compose(self) -> ComposeResult:
    yield Static("[Miscellaneous — coming soon]")
