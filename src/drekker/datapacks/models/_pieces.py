# Third party imports
from pydantic import BaseModel

# First party imports
from drekker.enumerated_constants.targets import NoteTarget
from drekker.enumerated_constants.triggers import Triggers
from drekker.project_vars import PYDANTIC_CONFIG


class DatapackPiece(BaseModel):
  """Base model for datapacks."""

  model_config = PYDANTIC_CONFIG


class RewardsEdge(DatapackPiece):
  rewards_on: Triggers
  reward_amount: int = 1
  temporary: bool = False
  situational: None | str = None

  extra: dict | None = None


class Note(DatapackPiece):
  target: NoteTarget
  content: str
