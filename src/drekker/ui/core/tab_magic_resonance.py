# Standard library imports
from typing import TYPE_CHECKING

# Third party imports
from textual.widgets import Static

# First party imports
from drekker.ui.core.core_base import CoreTabContainerBase

if TYPE_CHECKING:
  # Third party imports
  from textual.app import ComposeResult
  from textual.widget import Widget


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
