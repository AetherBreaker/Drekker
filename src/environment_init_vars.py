from logging import getLogger
from pathlib import Path
from sys import modules

from environment_settings import Settings

logger = getLogger(__name__)


# Settings
SETTINGS = Settings()  # type: ignore

# Folder paths
CWD = Path.cwd()


__main_loc = modules["__main__"].__file__
if __main_loc is None:
  raise RuntimeError("Could not determine __main__ location.")
__main_loc = Path(__main_loc)

if __main_loc.name != "__main__.py":
  if __debug__:
    __main_loc = CWD / "src"
  else:
    raise RuntimeError(f"Unexpected __main__ location: {__main_loc}")

MAIN_LOCATION = __main_loc.parent
