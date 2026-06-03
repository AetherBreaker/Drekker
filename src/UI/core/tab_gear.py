from textual.widgets import Static

from ui.core.core_base import CoreTabContainerBase
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from ui.core.tab_attributes import Widget
  from textual.app import ComposeResult


class GearTab(CoreTabContainerBase):
  """Equipment and gear management tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      "Gear",
      *children,
      name="gear",
      id="gear",
      disabled=disabled,
    )

  def compose(self) -> ComposeResult:
    yield Static("[Gear — coming soon]")
