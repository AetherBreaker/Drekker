# Standard library imports
from json import dump
from pathlib import Path
from typing import Annotated

# Third party imports
import typer
from pydantic import BaseModel, Field

# First party imports
from drekker.datapacks.models.qualities import Quality
from drekker.project_vars import PYDANTIC_CONFIG


class DatapackSerializer(BaseModel):
  model_config = PYDANTIC_CONFIG

  qualities: Annotated[list[Quality] | None, Field()] = None


DEFAULT_SCHEMA_OUTPUT_PATH = Path.cwd() / "datapack_schema.json"


def _generate_schemas(output_path: Path = DEFAULT_SCHEMA_OUTPUT_PATH) -> None:
  if not output_path.parent.exists():
    output_path.parent.mkdir(parents=True, exist_ok=True)
  with output_path.open("w") as f:
    dump(DatapackSerializer.model_json_schema(), f, indent=2)


def generate_schemas() -> None:
  typer.run(_generate_schemas)
