from project_vars import PYDANTIC_CONFIG
from pydantic import BaseModel


class DatapackUniversal(BaseModel):
  """Base model with Pydantic configuration."""

  model_config = PYDANTIC_CONFIG
