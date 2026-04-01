"""Gear tab for character sheet."""

from textual.app import ComposeResult
from textual.widgets import Static

from UI.core.core_base import CoreTabContainerBase
from UI.core.tab_attributes import Widget


class GearTab(CoreTabContainerBase):
  """Equipment and gear management tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      title="Gear",
      *children,
      name="gear",
      id="gear",
      disabled=disabled,
    )

  def compose(self) -> ComposeResult:
    yield Static("[Gear — coming soon]")
