"""Magic and Resonance tab for character sheet."""

from textual.app import ComposeResult
from textual.widgets import Static
from UI.core.core_base import CoreTabContainerBase


class MagicResonanceTab(CoreTabContainerBase):
  """Magical tradition, magic, resonance, and abilities tab."""

  def compose(self) -> ComposeResult:
    yield Static("[Magic & Resonance — coming soon]")
