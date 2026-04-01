from types import TracebackType

from textual.containers import ScrollableContainer
from textual.content import ContentType
from textual.widget import Widget
from textual.widgets import TabPane


class CoreTabContainerBase(TabPane):
  """Base class for all core TabbedContent panes.
  This is where we can add any shared functionality or styling for all tabs in the character
  sheet. For now, it's just a placeholder, but it allows us to easily add common features to
  all tabs in the future."""

  def __init__(
    self,
    title: ContentType,
    *children: Widget,
    name: str | None = None,
    id: str | None = None,
    classes: str | None = None,
    disabled: bool = False,
  ):
    self._container = ScrollableContainer(
      *children,
      name=f"{name}-container" if name else None,
      id=f"{id}-container" if id else None,
      classes=classes,
      disabled=disabled,
    )
    super().__init__(title, name=name, id=id, classes=classes, disabled=disabled)
