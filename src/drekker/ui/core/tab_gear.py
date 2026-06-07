# Standard library imports
from typing import TYPE_CHECKING

# Third party imports
from textual.widgets import Static

# First party imports
from drekker.ui.core.core_base import CoreTabContainerBase

if TYPE_CHECKING:
  # Third party imports
  from textual.app import ComposeResult

  # First party imports
  from drekker.ui.core.tab_attributes import Widget


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
