# Standard library imports
from typing import Annotated

# Third party imports
from pydantic import BaseModel, Field

# First party imports
from drekker.datapacks.models._pieces import Note, RewardsEdge
from drekker.project_vars import PYDANTIC_CONFIG


class Datapack(BaseModel):
  """Base model with Pydantic configuration."""

  model_config = PYDANTIC_CONFIG

  rewards_edge: Annotated[RewardsEdge | None, Field()] = None
  notes: Annotated[list[Note] | None, Field()] = None
