"""Gear tab for character sheet."""

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static

from UI.core.core_base import CoreTabContainerBase


class MatrixTab(CoreTabContainerBase):
  """Matrix and Matrix Gear management tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      title="Matrix",
      *children,
      name="matrix",
      id="matrix",
      disabled=disabled,
    )

  def compose(self) -> ComposeResult:
    yield Static("[Matrix — coming soon]")
