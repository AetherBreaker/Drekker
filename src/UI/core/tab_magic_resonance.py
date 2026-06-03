from textual.widgets import Static

from ui.core.core_base import CoreTabContainerBase
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from textual.widget import Widget
  from textual.app import ComposeResult


class MagicResonanceTab(CoreTabContainerBase):
  """Magical tradition, magic, resonance, and abilities tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      "Magic & Resonance",  # TODO Magic and Resonance are mutually exclusive
      *children,
      name="magic_resonance",  # TODO Magic and Resonance are mutually exclusive
      id="magic_resonance",  # TODO Magic and Resonance are mutually exclusive
      disabled=disabled,
    )

  def compose(self) -> ComposeResult:
    yield Static("[Magic & Resonance — coming soon]")
