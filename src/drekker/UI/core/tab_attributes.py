"""Attributes tab for character sheet."""

from textual.app import ComposeResult
from textual.widgets import Static
from UI.core.core_base import CoreTabContainerBase


class AttributesTab(CoreTabContainerBase):
  """Attributes, Qualities, and derived statistics tab."""

  def compose(self) -> ComposeResult:
    yield Static("[Attributes — coming soon]")
