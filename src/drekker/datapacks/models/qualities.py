# First party imports
from drekker.datapacks.enums import Sources
from drekker.datapacks.models import Datapack

type SubOptionLabel = str


class Quality(Datapack):
  """Base model for quality datapacks."""

  name: str

  # This should generally always be None or missing when loading from a datapack, as this should
  # instead be loaded in from a localization file.
  description: str | None = None

  source: Sources
  page_number: int

  sub_options: dict[SubOptionLabel, QualitySubOption] | None = None


class QualitySubOption(Datapack):
  """Model for quality sub-options."""

  name: str

  # This should generally always be None or missing when loading from a datapack, as this should
  # instead be loaded in from a localization file.
  description: str | None = None

  source: Sources | None = None  # If None, inherits from parent quality
  page_number: int | None = None  # If None, inherits from parent quality
