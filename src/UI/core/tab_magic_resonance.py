if __name__ == "__main__":
  from logging_config import configure_logging

  configure_logging()

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static

from ui.core.core_base import CoreTabContainerBase


class MagicResonanceTab(CoreTabContainerBase):
  """Magical tradition, magic, resonance, and abilities tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      title="Magic & Resonance",  # TODO Magic and Resonance are mutually exclusive
      *children,
      name="magic_resonance",  # TODO Magic and Resonance are mutually exclusive
      id="magic_resonance",  # TODO Magic and Resonance are mutually exclusive
      disabled=disabled,
    )

  def compose(self) -> ComposeResult:
    yield Static("[Magic & Resonance — coming soon]")
