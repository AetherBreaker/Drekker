"""Core UI module containing reusable tab wrapper class."""

from pydantic.types import T
from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import TabbedContent, TabPane

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
    with TabbedContent():
      with TabPane(title="Attributes", id="attributes"):
        yield AttributesTab()
      with TabPane(title="Skills", id="skills"):
        yield SkillsTab()
      with TabPane(title="Augmentations", id="augmentations"):
        yield AugmentationsTab()
      with TabPane(title="Matrix", id="matrix"):
        yield MatrixTab()
      with TabPane(title="Gear", id="gear"):
        yield GearTab()
      with TabPane(title="Vehicles", id="vehicles"):
        yield VehiclesTab()
      with TabPane(title="Magic & Resonance", id="magic-resonance"):
        yield MagicResonanceTab()
      with TabPane(title="Miscellaneous", id="misc"):
        yield MiscTab()


class DrekkerCoreTab(TabbedContent): ...


DrekkerCoreTab.mount
