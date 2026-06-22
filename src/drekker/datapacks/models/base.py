# Third party imports
from pydantic import BaseModel

# First party imports
from drekker.project_vars import PYDANTIC_CONFIG


class DatapackBase(BaseModel):
  """Base model with Pydantic configuration."""

  model_config = PYDANTIC_CONFIG


class DatapackPiece(BaseModel):
  """Base model for datapacks."""

  model_config = PYDANTIC_CONFIG
