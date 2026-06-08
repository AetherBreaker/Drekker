if __name__ == "__main__":
  # First party imports
  from drekker.initialize import initialize

  PROJECT_NAME = "Drekker"
  LOGGING_TYPE = "per_run"
  MAX_WIDTH = 40

  initialize()

# First party imports
from drekker import DrekkerApp
from drekker.project_vars import SETTINGS

listening_for_debugger = False if SETTINGS.debug_wait_for_client else None


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
