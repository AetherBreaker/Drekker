if __name__ == "__main__":
  from logging_config import configure_logging

  configure_logging()

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static

from ui.core.core_base import CoreTabContainerBase


class AugmentationsTab(CoreTabContainerBase):
  """Augmentations and cyberware management tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      title="Augmentations",
      *children,
      name="augmentations",
      id="augmentations",
      disabled=disabled,
    )

  def compose(self) -> ComposeResult:
    yield Static("[Augmentations — coming soon]")
