# Standard library imports
from typing import TYPE_CHECKING, override

# Third party imports
from textual.screen import Screen
from textual.widgets import Footer, Header, TabbedContent

# First party imports
from drekker.ui.core.tab_attributes import AttributesTab
from drekker.ui.core.tab_augmentations import AugmentationsTab
from drekker.ui.core.tab_gear import GearTab
from drekker.ui.core.tab_magic_resonance import MagicResonanceTab
from drekker.ui.core.tab_matrix import MatrixTab
from drekker.ui.core.tab_misc import MiscTab
from drekker.ui.core.tab_skills import SkillsTab
from drekker.ui.core.tab_vehicles import VehiclesTab

if TYPE_CHECKING:
  # Third party imports
  from textual.app import ComposeResult


class DrekkerCore(Screen):
  """Base container for all core character sheet tabs.
  This is where we can add any shared functionality or styling for all tabs in the character
  sheet. For now, it's just a placeholder, but it allows us to easily add common features to
  all tabs in the future."""

  BORDER_TITLE = "DrekkerCore"

  @override
  def compose(self) -> ComposeResult:
    yield Header()
    yield CoreTabs()
    yield Footer()


class CoreTabs(TabbedContent):
  BORDER_TITLE = "CoreTabs"

  async def on_mount(self) -> None:
    await self.add_pane(AttributesTab())
    await self.add_pane(SkillsTab())
    await self.add_pane(AugmentationsTab())
    await self.add_pane(MatrixTab())
    await self.add_pane(GearTab())
    await self.add_pane(VehiclesTab())
    await self.add_pane(MagicResonanceTab())
    await self.add_pane(MiscTab())

    self.active = "attributes"
