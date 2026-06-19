# Standard library imports
from logging import getLogger
from pathlib import Path
from sys import modules

# Third party imports
from pydantic import ConfigDict

# First party imports
from drekker.settings import Settings

logger = getLogger(__name__)


SETTINGS = Settings()

CWD = Path.cwd()
PYDANTIC_CONFIG = ConfigDict(
  populate_by_name=True,
  use_enum_values=True,
  validate_default=True,
  validate_assignment=True,
  coerce_numbers_to_str=True,
)


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
