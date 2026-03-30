"""Skills tab for character sheet."""

from textual.app import ComposeResult
from textual.widgets import Static
from UI.core.core_base import CoreTabContainerBase


class SkillsTab(CoreTabContainerBase):
  """Active skills management tab."""

  def compose(self) -> ComposeResult:
    yield Static("[Skills — coming soon]")
