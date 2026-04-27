from pydantic import BaseModel, ConfigDict
from pydantic.root_model import RootModel

PYDANTIC_CONFIG = ConfigDict(
  populate_by_name=True,
  use_enum_values=True,
  validate_default=True,
  validate_assignment=True,
  coerce_numbers_to_str=True,
)


class ConfiguredBaseModel(BaseModel):
  """Base model with Pydantic configuration."""

  model_config = PYDANTIC_CONFIG


class ConfiguredRootModel(RootModel):
  """Root model with Pydantic configuration."""

  model_config = PYDANTIC_CONFIG
