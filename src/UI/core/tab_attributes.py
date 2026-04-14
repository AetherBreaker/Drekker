"""Attributes tab for character sheet."""

from re import sub

from textual.app import ComposeResult
from textual.containers import Container, Grid, HorizontalGroup, Middle, VerticalGroup
from textual.widget import Widget
from textual.widgets import Button, Label

from UI.core.core_base import CoreTabContainerBase


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

  def compose(self) -> ComposeResult:
    with VerticalGroup(classes="test vert1") as vert1:
      vert1.border_title = "vert1"
      with HorizontalGroup(classes="test horz2") as horz2:
        horz2.border_title = "horz2"
        with Container(
          id="basic-data-container", classes="test placeholder"
        ) as placeholder:
          placeholder.border_title = "placeholder"
        with Container(
          id="appearance-container", classes="test placeholder"
        ) as placeholder:
          placeholder.border_title = "placeholder"
      with HorizontalGroup(classes="test horz2") as horz2:
        horz2.border_title = "horz2"
        with VerticalGroup(classes="test vert3") as vert3:
          vert3.border_title = "vert3"
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
        with VerticalGroup(classes="test vert3") as vert3:
          vert3.border_title = "vert3"
          with Container(
            id="qualities-container", classes="test placeholder"
          ) as placeholder:
            placeholder.border_title = "placeholder"
        with VerticalGroup(classes="test vert3") as vert3:
          vert3.border_title = "vert3"
          with Container(
            id="quality-paths-container", classes="test placeholder"
          ) as placeholder:
            placeholder.border_title = "placeholder"
          with Container(
            id="critter-powers-container", classes="test placeholder"
          ) as placeholder:
            placeholder.border_title = "placeholder"


class AttrTable(Grid):
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

    self.attributes = [
      {
        "display_name": attr.title(),
        "id": sub(" +", "-", attr.lower()),
        "value": 0,
      }
      for attr in attributes
    ]
    # self.styles.grid_size_rows = len(self.attributes)
    # self.styles.grid_size_columns = 4

  def compose(self) -> ComposeResult:
    for attr in self.attributes:
      with Middle():
        yield Label(
          attr["display_name"],
          expand=False,
          shrink=False,
          id=f"{attr['id']}-label",
          classes="attr-label attr-row",
        )
      yield Button(
        "+", id=f"{attr['id']}-increment", classes="attr-inc attr-row attr-button"
      )
      with Middle():
        yield Label(
          f"{attr['value']}", id=f"{attr['id']}-value", classes="attr-value attr-row"
        )
      yield Button(
        "-", id=f"{attr['id']}-decrement", classes="attr-dec attr-row attr-button"
      )
