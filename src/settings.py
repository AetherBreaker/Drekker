import os
from logging import getLogger
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

logger = getLogger(__name__)

os.environ.setdefault("PYDANTIC_ERRORS_INCLUDE_URL", "false")


class Settings(BaseSettings):
  model_config = SettingsConfigDict(
    env_file=Path.cwd() / ".env",
    env_file_encoding="utf-8",
    env_ignore_empty=True,
    extra="ignore",
  )

  debug_wait_for_client: bool = False
