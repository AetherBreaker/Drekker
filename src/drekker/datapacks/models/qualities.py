# Standard library imports
import operator
from enum import auto
from functools import reduce
from typing import TYPE_CHECKING

# Third party imports
from pydantic import model_validator

# First party imports
from drekker.datapacks.enums import Sources
from drekker.datapacks.models import Datapack
from drekker.datapacks.models._pieces import DatapackPiece
from drekker.enumerated_constants.targets import ModificationTarget
from drekker.typing import StrEnumBase

if TYPE_CHECKING:
  # Standard library imports
  from typing import Any

  # Third party imports
  from pydantic import GetJsonSchemaHandler
  from pydantic_core import core_schema as cs


class QualityKind(StrEnumBase):
  POSITIVE = auto()
  NEGATIVE = auto()


class QualityCategory(StrEnumBase):
  ADEPT_WAYS = auto(), "Street Wyrd"
  CHARACTER_TRAITS = auto(), "Shadow Cast"
  DRAKE = auto(), "Lofwyr's Legions"
  HMHVV_INFECTED = auto(), "Companion"
  LIFESTYLE = auto()
  MARTIAL_ART = auto()
  SURGE = auto(), "Companion"
  REGULAR = auto(), "Regular Qualities"
  SHIFTER = auto(), "Shifter Qualities"
  STREAMS = auto(), "Technomancer Streams - Hack N Slash"
  TRANSGENIC = auto(), "Body Shop"
  VIRTUAL_LIFE = auto(), "AI/EI - Hack N Slash"


class QualitySurgeSubcategory(StrEnumBase):
  ANIMAL_PELAGE = auto(), "Animal Pelage"
  BENEFICIAL_SECRETIONS = auto(), "Beneficial Secretions"
  COMPLEX_TRAITS = auto(), "Complex Traits"
  DERMAL_ALTERATION = auto(), "Dermal Alterations"
  METAGENIC_SENSES = auto(), "Metagenic Senses"
  METAGENIC_MORPHISMS = auto(), "Metagenic Morphisms"
  AHD = auto(), "Aural Helix Dysmorphia (AHD)"
  BIOLOGICAL_DYSMORPHIA = auto(), "Biological Dysmorphia"
  METAGENIC_ANOMALIES = auto(), "Metagenic Anomalies"
  METAGENIC_DEFECTS = auto(), "Metagenic Defects"
  METAGENIC_THROWBACKS = auto(), "Metagenic Throwbacks"
  NEUROPATHIC_ADJUSTED_STATES = auto(), "Neuropathic Adjusted States (NAS)"


# Maps QualityCategory values to their subcategory enum class.
# To add subcategories for a new category, define a new StrEnumBase subclass
# and add a single entry here — the field type, validator, and JSON schema
# all update automatically.
SUBCATEGORY_MAP: dict[QualityCategory, type[StrEnumBase]] = {
  QualityCategory.SURGE: QualitySurgeSubcategory,
}

_AnySubcategory = reduce(operator.or_, SUBCATEGORY_MAP.values())


class Quality(Datapack):
  """Base model for quality datapacks."""

  name: str

  # This should generally always be None or missing when loading from a datapack, as this should
  # instead be loaded in from a localization file.
  description: str | None = None

  kind: QualityKind
  category: QualityCategory
  subcategory: _AnySubcategory | None = None  # type: ignore[valid-type]

  karma: int

  source: Sources
  page_number: int

  sub_options: list[QualitySubOption] | None = None

  @model_validator(mode="after")
  def _validate_subcategory(self) -> Quality:
    if self.subcategory is None:
      return self
    allowed = SUBCATEGORY_MAP.get(self.category)
    if allowed is None:
      raise ValueError(f"subcategory is not valid for category={self.category!r}")
    if not isinstance(self.subcategory, allowed):
      raise ValueError(f"subcategory must be a {allowed.__name__} value for category={self.category!r}")
    return self

  @classmethod
  def __get_pydantic_json_schema__(cls, core_schema: cs.CoreSchema, handler: GetJsonSchemaHandler) -> dict[str, Any]:
    json_schema = handler(core_schema)
    json_schema = handler.resolve_ref_schema(json_schema)
    if not SUBCATEGORY_MAP:
      return json_schema

    subcategory_any_of = json_schema.get("properties", {}).get("subcategory", {}).get("anyOf", [])
    null_schema: dict[str, Any] = {"type": "null"}

    def _schema_for(sub_cls: type[StrEnumBase]) -> dict[str, Any]:
      """Find the anyOf entry that was generated for sub_cls by matching its member values."""
      member_values = {m.value for m in sub_cls}
      for entry in subcategory_any_of:
        if entry == null_schema:
          continue
        values = {e["const"] for e in entry.get("oneOf", []) if "const" in e} or set(entry.get("enum", []))
        if values == member_values:
          return entry
      return null_schema

    def _build(items: list[tuple[QualityCategory, type[StrEnumBase]]]) -> dict[str, Any]:
      """Recursively build nested if/then/else for each mapped category."""
      if not items:
        return {"properties": {"subcategory": null_schema}}
      (category, sub_cls), *rest = items
      return {
        "if": {"properties": {"category": {"const": category.value}}},
        "then": {"properties": {"subcategory": _schema_for(sub_cls)}},
        "else": _build(rest),
      }

    json_schema.update(_build(list(SUBCATEGORY_MAP.items())))
    return json_schema


class QualitySubOption(Datapack):
  """Model for quality sub-options."""

  name: str

  # If None, inherits from parent quality's karma. If both are None, validation should fail
  karma: int | None = None

  # If True, this sub-option's karma replaces the parent quality's karma instead of adding to it.
  overwrite_parent_karma: bool = False

  # This should generally always be None or missing when loading from a datapack, as this should
  # instead be loaded in from a localization file.
  description: str | None = None

  source: Sources | None = None  # If None, inherits from parent quality
  page_number: int | None = None  # If None, inherits from parent quality


class Modification(DatapackPiece):
  target: ModificationTarget
