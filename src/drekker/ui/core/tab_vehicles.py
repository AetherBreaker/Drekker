# Standard library imports
from typing import TYPE_CHECKING, override

# Third party imports
from textual.widgets import Static

# First party imports
from drekker.ui.core.core_base import CoreTabContainerBase

if TYPE_CHECKING:
  # Third party imports
  from textual.app import ComposeResult
  from textual.widget import Widget


class VehiclesTab(CoreTabContainerBase):
  """Vehicles management tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      "Vehicles",
      *children,
      name="vehicles",
      id="vehicles",
      disabled=disabled,
    )

  @override
  def compose(self) -> ComposeResult:
    yield Static("[Vehicles — coming soon]")
