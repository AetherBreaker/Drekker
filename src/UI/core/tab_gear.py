if __name__ == "__main__":
  from logging_config import configure_logging

  configure_logging()

from textual.app import ComposeResult
from textual.widgets import Static

from ui.core.core_base import CoreTabContainerBase
from ui.core.tab_attributes import Widget


class GearTab(CoreTabContainerBase):
  """Equipment and gear management tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      title="Gear",
      *children,
      name="gear",
      id="gear",
      disabled=disabled,
    )

  def compose(self) -> ComposeResult:
    yield Static("[Gear — coming soon]")
