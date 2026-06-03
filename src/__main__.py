from collections.abc import Callable
from typing import ClassVar, TYPE_CHECKING

from project_vars import MAIN_LOCATION, SETTINGS
from textual.app import App
from ui.core import DrekkerCore

if TYPE_CHECKING:
  from textual.screen import Screen
  from textual._path import CSSPathType

listening_for_debugger = False if SETTINGS.debug_wait_for_client else None


class DrekkerApp(App[None]):
  """Main Shadowrun 6E character sheet application."""

  DEFAULT_MODE = "Sheet"
  MODES: ClassVar[dict[str, str | Callable[[], Screen]]] = {
    "Sheet": DrekkerCore,
  }
  CSS_PATH: ClassVar[CSSPathType | None] = [
    MAIN_LOCATION / "drekker.tcss",
    MAIN_LOCATION / "ui" / "core" / "core_tabs.tcss",
  ]

  def __init__(self) -> None:
    global listening_for_debugger
    if not listening_for_debugger and listening_for_debugger is not None:
      import debugpy

      listening_for_debugger = True
      debugpy.connect(("127.0.0.1", 5678))
      debugpy.wait_for_client()
    super().__init__()


def startup() -> None:
  global listening_for_debugger
  if not listening_for_debugger and listening_for_debugger is not None:
    import debugpy

    listening_for_debugger = True
    debugpy.connect(("127.0.0.1", 5678))
    debugpy.wait_for_client()

  app = DrekkerApp()
  app.run()


if __name__ == "__main__":
  startup()
