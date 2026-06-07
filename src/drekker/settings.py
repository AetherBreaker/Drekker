# Standard library imports
import os
import sys
from logging import getLogger
from pathlib import Path
from typing import Annotated

# Third party imports
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = getLogger(__name__)

os.environ.setdefault("PYDANTIC_ERRORS_INCLUDE_URL", "false")

CWD = Path(__file__).parent if getattr(sys, "frozen", False) else Path.cwd()


class Settings(BaseSettings):
  model_config = SettingsConfigDict(
    env_file=Path.cwd() / ".env",
    env_file_encoding="utf-8",
    env_ignore_empty=True,
    extra="ignore",
  )

  debug_wait_for_client: bool = False
  log_loc_folder: Annotated[Path, Field(alias="LOG_LOC_FOLDER")] = CWD / "logs"
