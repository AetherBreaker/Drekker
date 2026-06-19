# Standard library imports
from enum import StrEnum
from typing import TYPE_CHECKING, override

# Third party imports
from pydantic_core import core_schema as cs

if TYPE_CHECKING:
  # Standard library imports
  from typing import Any, Self

  # Third party imports
  from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler


class StrEnumBase(StrEnum):
  description: str

  def __new__(cls, value: str, description: str = "") -> Self:
    obj = str.__new__(cls, value)
    obj._value_ = value
    obj.description = description
    return obj

  @override
  @staticmethod
  def _generate_next_value_(name: str, start: int, count: int, last_values: list[str]) -> str:
    return name.upper()

  @classmethod
  def __get_pydantic_core_schema__(cls, source_type: Any, handler: GetCoreSchemaHandler) -> cs.CoreSchema:
    return cs.enum_schema(cls, list(cls))

  @classmethod
  def __get_pydantic_json_schema__(cls, core_schema: cs.CoreSchema, handler: GetJsonSchemaHandler) -> dict[str, Any]:
    schema = handler(core_schema)
    if any(getattr(m, "description", "") for m in cls):
      return {
        "oneOf": [
          {
            "const": m.value,
            **({"description": m.description} if getattr(m, "description", "") else {}),
          }
          for m in cls
        ]
      }
    return schema
