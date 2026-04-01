"""Main UI module for Drekker character sheet.

This module manages the composition and layout of all UI tabs and main interface elements.
"""

from textual.app import ComposeResult
from textual.containers import Container

from UI.core import DrekkerCore


class DrekkerBaseViewport(Container):
  def compose(self) -> ComposeResult:
    yield DrekkerCore()
