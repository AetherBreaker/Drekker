from asyncio import set_event_loop
from sys import platform

import debugpy
from environment_init_vars import MAIN_LOCATION, SETTINGS
from textual.app import App, ComposeResult
from UI import DrekkerBaseViewport

if platform in ("win32", "cygwin", "cli"):
  from winloop import new_event_loop
else:
  from uvloop import new_event_loop  # type: ignore

set_event_loop(new_event_loop())


listening_for_debugger = False if SETTINGS.debug_wait_for_client else None


class DrekkerApp(App[None]):
  """Main Shadowrun 6E character sheet application."""

  CSS_PATH = [
    # MAIN_LOCATION / "drekker.tcss",
    MAIN_LOCATION / "UI" / "core" / "core_tabs.tcss",
  ]

  def __init__(self) -> None:
    global listening_for_debugger
    if not listening_for_debugger and listening_for_debugger is not None:
      listening_for_debugger = True
      debugpy.connect(("127.0.0.1", 5678))
      debugpy.wait_for_client()
    super().__init__()

  def compose(self) -> ComposeResult:
    """Compose the main application layout."""
    yield DrekkerBaseViewport()


def startup() -> None:
  global listening_for_debugger
  if not listening_for_debugger and listening_for_debugger is not None:
    listening_for_debugger = True
    debugpy.connect(("127.0.0.1", 5678))
    debugpy.wait_for_client()

  app = DrekkerApp()
  app.run()


if __name__ == "__main__":
  startup()
