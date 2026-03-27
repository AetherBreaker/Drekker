from asyncio import set_event_loop
from sys import platform

import debugpy
from textual.app import App, ComposeResult
from textual.widgets import Footer, Markdown, TabbedContent, TabPane

TAB_NAMES = (
  "cross",
  "horizontal",
  "custom",
  "left",
  "right",
)


class TabsApp(App):
  """Demonstrates the Tabs widget."""

  CSS_PATH = "tabs.tcss"

  BINDINGS = []

  def compose(self) -> ComposeResult:
    with TabbedContent(classes="tabs"):
      for tab_name in TAB_NAMES:
        with TabPane(tab_name, classes=f"hatch {tab_name}"):
          yield Markdown("test text", classes="content")
    yield Footer()

  def on_mount(self) -> None:
    """Focus the tabs when the app starts."""
    self.query_one(TabbedContent).focus()


if __name__ == "__main__":
  if __debug__:
    debugpy.listen(("127.0.0.1", 5678))
    debugpy.wait_for_client()
    debugpy.is_client_connected()
  if platform in ("win32", "cygwin", "cli"):
    from winloop import new_event_loop
  else:
    # if we're on apple or linux do this instead
    from uvloop import new_event_loop  # type: ignore

  set_event_loop(new_event_loop())

  app = TabsApp()
  app.run()
