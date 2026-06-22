# Standard library imports
from typing import Annotated

# Third party imports
from pydantic import Field

# First party imports
from drekker.datapacks.models.base import DatapackBase
from drekker.project_vars import PYDANTIC_CONFIG
from drekker.systems.sr6.datapacks.models.parts import Note, RewardsEdge


class Datapack(DatapackBase):
  """Base model with Pydantic configuration."""

  model_config = PYDANTIC_CONFIG

  rewards_edge: Annotated[RewardsEdge | None, Field()] = None
  notes: Annotated[list[Note] | None, Field()] = None
