"""Gear tab for character sheet."""

from textual.app import ComposeResult
from textual.widgets import Static
from UI.core.core_base import CoreTabContainerBase


class MatrixTab(CoreTabContainerBase):
  """Matrix and Matrix Gear management tab."""

  def compose(self) -> ComposeResult:
    yield Static("[Matrix — coming soon]")
