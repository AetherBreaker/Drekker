# First party imports
from drekker.datapacks.models.base import DatapackPiece
from drekker.systems.sr6.enumerated_constants.targets import NoteTarget
from drekker.systems.sr6.enumerated_constants.triggers import Triggers


class RewardsEdge(DatapackPiece):
  rewards_on: Triggers
  reward_amount: int = 1
  temporary: bool = False
  situational: None | str = None

  extra: dict | None = None


class Note(DatapackPiece):
  target: NoteTarget
  content: str
