from textual.binding import Binding
from textual.content import ContentType
from textual.widget import Widget
from textual.widgets import TabPane


class CoreTabContainerBase(TabPane):
  """Base class for all core TabbedContent panes.
  This is where we can add any shared functionality or styling for all tabs in the character
  sheet. For now, it's just a placeholder, but it allows us to easily add common features to
  all tabs in the future."""

  BORDER_TITLE = "CoreTabContainerBase"

  BINDINGS = [
    Binding("up", "scroll_up", "Scroll Up", show=False),
    Binding("down", "scroll_down", "Scroll Down", show=False),
    Binding("left", "scroll_left", "Scroll Left", show=False),
    Binding("right", "scroll_right", "Scroll Right", show=False),
    Binding("home", "scroll_home", "Scroll Home", show=False),
    Binding("end", "scroll_end", "Scroll End", show=False),
    Binding("pageup", "page_up", "Page Up", show=False),
    Binding("pagedown", "page_down", "Page Down", show=False),
    Binding("ctrl+pageup", "page_left", "Page Left", show=False),
    Binding("ctrl+pagedown", "page_right", "Page Right", show=False),
  ]

  def __init__(
    self,
    title: ContentType,
    *children: Widget,
    name: str | None = None,
    id: str | None = None,
    classes: str | None = None,
    disabled: bool = False,
  ):
    super().__init__(
      title, *children, name=name, id=id, classes=classes, disabled=disabled
    )
