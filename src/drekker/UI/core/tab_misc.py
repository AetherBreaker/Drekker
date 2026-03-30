"""Identity tab for character sheet."""

from textual.app import ComposeResult
from textual.widgets import Static
from UI.core.core_base import CoreTabContainerBase


class MiscTab(CoreTabContainerBase):
  """Identity information, notes, and miscellaneous tab."""

  def compose(self) -> ComposeResult:
    yield Static("[Miscellaneous — coming soon]")
