# Standard library imports
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  # First party imports
  from drekker.logging.logging_config import QueueCatchall


def initialize(*queues: QueueCatchall):
  # Standard library imports
  from asyncio import set_event_loop
  from os import environ
  from sys import platform

  # First party imports
  from drekker.logging.init_logging import init_logging

  environ.setdefault("PYDANTIC_ERRORS_INCLUDE_URL", "false")

  if platform in ("win32", "cygwin", "cli"):
    # Third party imports
    from winloop import new_event_loop
  else:
    # Third party imports
    from uvloop import new_event_loop  # type: ignore

  set_event_loop(new_event_loop())

  init_logging(*queues)
