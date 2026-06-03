from textual.widgets import Static

from ui.core.core_base import CoreTabContainerBase
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from textual.widget import Widget
  from textual.app import ComposeResult


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
