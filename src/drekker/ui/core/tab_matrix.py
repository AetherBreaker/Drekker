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


class MatrixTab(CoreTabContainerBase):
  """Matrix and Matrix Gear management tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      "Matrix",
      *children,
      name="matrix",
      id="matrix",
      disabled=disabled,
    )

  def compose(self) -> ComposeResult:
    yield Static("[Matrix — coming soon]")
