if __name__ == "__main__":
  # First party imports
  from drekker.initialize import initialize

  PROJECT_NAME = "Drekker"
  LOGGING_TYPE = "per_run"
  MAX_WIDTH = 40

  initialize()

# Standard library imports
from typing import TYPE_CHECKING, ClassVar

# Third party imports
from textual.app import App

# First party imports
from drekker.project_vars import MAIN_LOCATION, SETTINGS
from drekker.ui.core import DrekkerCore

if TYPE_CHECKING:
  # Standard library imports
  from collections.abc import Callable

  # Third party imports
  from textual._path import CSSPathType
  from textual.screen import Screen

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
      # Third party imports
      import debugpy  # noqa: T100

      listening_for_debugger = True
      debugpy.connect(("127.0.0.1", 5678))
      debugpy.wait_for_client()  # noqa: T100
    super().__init__()


def startup() -> None:
  global listening_for_debugger
  if not listening_for_debugger and listening_for_debugger is not None:
    # Third party imports
    import debugpy  # noqa: T100

    listening_for_debugger = True
    debugpy.connect(("127.0.0.1", 5678))
    debugpy.wait_for_client()  # noqa: T100

  app = DrekkerApp()
  app.run()


if __name__ == "__main__":
  startup()
