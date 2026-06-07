# Standard library imports
from typing import Annotated

# Third party imports
from pydantic import BaseModel, Field

# First party imports
from drekker.datapacks.models.qualities import Quality
from drekker.project_vars import PYDANTIC_CONFIG


class DatapackSerializer(BaseModel):
  model_config = PYDANTIC_CONFIG

  qualities: Annotated[list[Quality] | None, Field()] = None
