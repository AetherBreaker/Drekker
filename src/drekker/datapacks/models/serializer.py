# Standard library imports
from json import dump
from pathlib import Path

# Third party imports
import typer
from pydantic import BaseModel, Field

# First party imports
from drekker.project_vars import PYDANTIC_CONFIG
from drekker.systems.sr6.datapacks.models.gear import AnyGear
from drekker.systems.sr6.datapacks.models.qualities import Quality


class DatapackSerializer(BaseModel):
  model_config = PYDANTIC_CONFIG

  qualities: list[Quality] | None = Field(
    default=None,
    description="""A list of qualities that the datapack has.
    This can be used to determine which features to enable or disable when loading the datapack.""",
  )

  gear: list[AnyGear] | None = Field(
    default=None,
    description="A list of gear items defined by this datapack.",
  )


DEFAULT_SCHEMA_OUTPUT_PATH = Path.cwd() / "datapack_schema.json"


def _generate_schemas(output_path: Path = DEFAULT_SCHEMA_OUTPUT_PATH) -> None:
  if not output_path.parent.exists():
    output_path.parent.mkdir(parents=True, exist_ok=True)
  with output_path.open("w") as f:
    dump(DatapackSerializer.model_json_schema(), f, indent=2)


def generate_schemas() -> None:
  typer.run(_generate_schemas)
