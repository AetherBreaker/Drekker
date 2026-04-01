"""Attributes tab for character sheet."""

from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.widget import Widget
from textual.widgets import Static

from UI.core.core_base import CoreTabContainerBase


class AttributesTab(CoreTabContainerBase):
  """Attributes, Qualities, and derived statistics tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      title="Attributes",
      *children,
      name="attributes",
      id="attributes",
      disabled=disabled,
    )

  def compose(self) -> ComposeResult:
    with ScrollableContainer():
      yield Static("[Attributes — coming soon]")
