"""Core UI module containing reusable tab wrapper class."""

from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import TabbedContent

from UI.core.tab_attributes import AttributesTab
from UI.core.tab_augmentations import AugmentationsTab
from UI.core.tab_gear import GearTab
from UI.core.tab_magic_resonance import MagicResonanceTab
from UI.core.tab_matrix import MatrixTab
from UI.core.tab_misc import MiscTab
from UI.core.tab_skills import SkillsTab
from UI.core.tab_vehicles import VehiclesTab


class DrekkerCore(Container):
  """Base container for all core character sheet tabs.
  This is where we can add any shared functionality or styling for all tabs in the character
  sheet. For now, it's just a placeholder, but it allows us to easily add common features to
  all tabs in the future."""

  def compose(self) -> ComposeResult:
    yield CoreTabs()


class CoreTabs(TabbedContent):
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
