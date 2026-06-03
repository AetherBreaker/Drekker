from textual.widgets import Static

from ui.core.core_base import CoreTabContainerBase
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from textual.widget import Widget
  from textual.app import ComposeResult


class AugmentationsTab(CoreTabContainerBase):
  """Augmentations and cyberware management tab."""

  def __init__(
    self,
    *children: Widget,
    disabled: bool = False,
  ):
    super().__init__(
      "Augmentations",
      *children,
      name="augmentations",
      id="augmentations",
      disabled=disabled,
    )

  def compose(self) -> ComposeResult:
    yield Static("[Augmentations — coming soon]")
