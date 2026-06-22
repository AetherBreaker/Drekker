# First party imports
from drekker.typing import StrEnumBase


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
  BODY_SHOP = "Body Shop"
  DOUBLE_CLUTCH = "Double Clutch"
  STREET_WYRD = "Street Wyrd"
  SHADOW_CAST = "Shadow Cast"
  SMOOTH_OPERATIONS = "Smooth Operations"
  DEADLY_ART = "Deadly Arts"
  DEALERS_OF_DEATH = "Dealers of Death"
  KRIME_KATALOG = "Krime Katalog"
  ASTRAL_WAYS = "Astral Ways"
  SLIP_STREAMS = "Slip Streams"
  POWER_PLAYS = "Power Plays"
  TARNISHED_STAR = "Tarnished Star"
  EMERALD_CITY = "Emerald City"
