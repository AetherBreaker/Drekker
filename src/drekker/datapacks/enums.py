# Standard library imports
from enum import auto

# First party imports
from drekker.typing.enums import StrEnumBase


class Sources(StrEnumBase):
  """Enum for sources that can be used in the datapack."""

  SIXTH_WORLD_COMPANION = "Sixth World Companion"
  CORE_RULEBOOK_ANY = "Core Rulebook (Any Edition)"
  CORE_RULEBOOK_BERLIN = "Core Rulebook (Berlin Edition)"
  CORE_RULEBOOK_HONG_KONG = "Core Rulebook (Hong Kong Edition)"
  CORE_RULEBOOK_SEATTLE = "Core Rulebook (Seattle Edition)"
  HACK_N_SLASH = "Hack'n Slash"
  NO_FUTURE = "No Future"
  FIRING_SQUAD = "Firing Squad"
