from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static

from ui.core.core_base import CoreTabContainerBase


class SkillsTab(CoreTabContainerBase):
  """Active skills management tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      title="Skills",
      *children,
      name="skills",
      id="skills",
      disabled=disabled,
    )

  def compose(self) -> ComposeResult:
    yield Static("[Skills — coming soon]")
