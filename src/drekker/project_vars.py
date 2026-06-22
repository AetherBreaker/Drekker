# Standard library imports
from logging import getLogger
from pathlib import Path

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


# travel up the path until we find a folder named "drekker"
try:
  __drekker_package_loc = next(p for p in Path(__file__).parents if p.name == "drekker")
except StopIteration:
  raise RuntimeError("Could not find 'drekker' package in the path hierarchy.") from None

MAIN_LOCATION = __drekker_package_loc
