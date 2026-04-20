if __name__ == "__main__":
  from logging_config import configure_logging

  configure_logging()

from re import sub

from textual.app import ComposeResult
from textual.containers import Container, HorizontalGroup, VerticalGroup
from textual.widget import Widget
from textual.widgets import Button, Label

from ui.core.core_base import CoreTabContainerBase


class AttributesTab(CoreTabContainerBase):
  """Attributes, Qualities, and derived statistics tab."""

  BORDER_TITLE = "AttributesTab"

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

  def compose(self) -> ComposeResult:  # sourcery skip: extract-duplicate-method
    with VerticalGroup(classes="test vert1") as vert1:
      vert1.border_title = "vert1"
      with HorizontalGroup(classes="test horz2") as horz2:
        horz2.border_title = "horz2"
        with Container(id="basic-data-container", classes="test placeholder") as placeholder:
          placeholder.border_title = "placeholder"
        with Container(id="appearance-container", classes="test placeholder") as placeholder:
          placeholder.border_title = "placeholder"
      with HorizontalGroup(classes="test horz2") as horz2:
        horz2.border_title = "horz2"
        with VerticalGroup(classes="test vert3") as vert3:
          vert3.border_title = "vert3"
          vert3.styles.overflow_y = "scroll"
          vert3.styles.overflow_x = "scroll"
          with HorizontalGroup(classes="test horz3") as horz3:
            horz3.border_title = "horz3"
            yield AttrTable(
              "Body",
              "Agility",
              "Reaction",
              "Strength",
              "Willpower",
              "Logic",
              "Intuition",
              "Charisma",
              "Edge",
              "Magic",
              "Resonance",
            )
            with Container(id="qualities-container", classes="test placeholder") as placeholder:
              placeholder.border_title = "placeholder"
        with VerticalGroup(classes="test vert3") as vert3:
          vert3.border_title = "vert3"
          with Container(id="qualities-container", classes="test placeholder") as placeholder:
            placeholder.border_title = "placeholder"
        with VerticalGroup(classes="test vert3") as vert3:
          vert3.border_title = "vert3"
          with Container(id="quality-paths-container", classes="test placeholder") as placeholder:
            placeholder.border_title = "placeholder"
          with Container(id="critter-powers-container", classes="test placeholder") as placeholder:
            placeholder.border_title = "placeholder"


class AttrTable(HorizontalGroup):
  """Table for displaying attributes and their values."""

  BORDER_TITLE = "AttrTable"

  def __init__(
    self,
    *attributes: str,
    name: str | None = None,
    id: str | None = None,
    classes: str | None = None,
    disabled: bool = False,
  ):
    super().__init__(name=name, id=id, classes=classes, disabled=disabled)

    self.attributes = {
      sub(" +", "-", attr.lower()): {
        "display_name": attr.title(),
        "value": 0,
      }
      for attr in attributes
    }

  class AttrColumn(VerticalGroup):
    DEFAULT_CLASSES = "attr-col"
    DEFAULT_CSS = """
    AttrColumn {
      width: auto;
    }
    """

  class AttrLabelColumn(AttrColumn):
    DEFAULT_CSS = """
    AttrLabelColumn {
      align: left middle;
    }
    """

  class AttrValueColumn(AttrColumn):
    DEFAULT_CSS = """
    AttrValueColumn {
      align-horizontal: right;
    }
    """

  class AttrLabel(Label):
    DEFAULT_CLASSES = "attr-label"
    DEFAULT_CSS = """
    AttrLabel {
      padding: 1 1;
    }
    """

  class AttrButton(Button):
    DEFAULT_CLASSES = "attr-button"
    DEFAULT_CSS = """
    AttrButton {
      max-width: 5;
      max-height: 3;
      border: solid;
    }
    """

  class AttrValue(Label):
    DEFAULT_CLASSES = "attr-value"
    DEFAULT_CSS = """
    AttrValue {
      padding: 1;
      content-align-horizontal: right;
      # border: solid;
    }
    """

  def compose(self) -> ComposeResult:
    attr_labels = []
    attr_incs = []
    attr_values = []
    attr_decs = []
    for attr_id, attr in self.attributes.items():
      attr_labels.append(self.AttrLabel(attr["display_name"], id=f"{attr_id}-label"))
      attr_incs.append(self.AttrButton("+", id=f"{attr_id}-increment"))
      attr_values.append(self.AttrValue(f"{attr['value']}", id=f"{attr_id}-value", expand=True))
      attr_decs.append(self.AttrButton("-", id=f"{attr_id}-decrement"))
    with self.AttrLabelColumn():
      yield from attr_labels
    with self.AttrColumn():
      yield from attr_incs
    with self.AttrValueColumn():
      yield from attr_values
    with self.AttrColumn():
      yield from attr_decs

  # async def on_mount(self) -> None:
  #   self.styles.height = self.arrange(Size(23, 0)).total_region.height + 2

  async def on_button_pressed(self, event: Button.Pressed) -> None:
    button_id = event.button.id
    if button_id is None:
      return

    attr_id, action = button_id.split("-")

    attr_dat = self.attributes.get(attr_id)

    value = 1 if action == "increment" else -1

    if attr_dat is None:
      return

    self.query_one(f"#{attr_id}-value", Label).update(f"{attr_dat['value'] + value}")
    attr_dat["value"] += value
