# Standard library imports
from collections.abc import Generator, Iterable, Mapping

# Third party imports
from pydantic import BaseModel, RootModel

# First party imports
from drekker.project_vars import PYDANTIC_CONFIG
from drekker.sheets.sr6character import SR6Character


class ConfiguredBaseModel(BaseModel):
  """Base model with Pydantic configuration."""

  model_config = PYDANTIC_CONFIG

  _top: SR6Character = None  # type: ignore

  def _propogate_top(self) -> None:
    for _, field_value in self:
      match field_value:
        case ConfiguredBaseModel():
          field_value._top = self._top
          field_value._propogate_top()
        case ConfiguredRootModel():
          field_value._top = self._top
          field_value._propogate_top()
        case Mapping():
          for item in field_value.values():
            if isinstance(item, ConfiguredBaseModel):
              item._top = self._top
              item._propogate_top()
        case Iterable():
          for item in field_value:
            if isinstance(item, ConfiguredBaseModel):
              item._top = self._top
              item._propogate_top()
    self._post_init()

  def _post_init(self) -> None:
    """Called after the model is initialized. Can be used to set up any additional state or perform any additional validation."""
    pass


class ConfiguredRootModel[RootT](RootModel[RootT]):
  """Root model with Pydantic configuration."""

  model_config = PYDANTIC_CONFIG

  _top: SR6Character = None  # type: ignore

  def _propogate_top(self) -> None:
    raise NotImplementedError("Root models must implement their own _propogate_top method.")

  def _post_init(self) -> None:
    """Called after the model is initialized. Can be used to set up any additional state or perform any additional validation."""
    pass


class ConfiguredListModel[ContainedT](ConfiguredRootModel[list[ContainedT]]):
  """Root model for lists with Pydantic configuration."""

  root: list[ContainedT]

  def _propogate_top(self) -> None:
    for field_value in self.root:
      match field_value:
        case ConfiguredBaseModel():
          field_value._top = self._top
          field_value._propogate_top()
        case ConfiguredRootModel():
          field_value._top = self._top
          field_value._propogate_top()
        case Mapping():
          for item in field_value.values():
            if isinstance(item, ConfiguredBaseModel):
              item._top = self._top
              item._propogate_top()
        case Iterable():
          for item in field_value:
            if isinstance(item, ConfiguredBaseModel):
              item._top = self._top
              item._propogate_top()
    self._post_init()

  def __iter__(self) -> Generator[ContainedT]:  # type: ignore
    yield from self.root

  def __getitem__(self, index: int) -> ContainedT:
    return self.root[index]

  def __setitem__(self, key: int, value: ContainedT) -> None:
    self.root[key] = value
    if isinstance(value, (ConfiguredBaseModel, ConfiguredRootModel)):
      value._top = self._top
      value._propogate_top()

  def __len__(self) -> int:
    return len(self.root)

  def append(self, item: ContainedT) -> None:
    if isinstance(item, (ConfiguredBaseModel, ConfiguredRootModel)):
      item._top = self._top
      item._propogate_top()
    self.root.append(item)

  def extend(self, items: Iterable[ContainedT]) -> None:
    for item in items:
      if isinstance(item, (ConfiguredBaseModel, ConfiguredRootModel)):
        item._top = self._top
        item._propogate_top()
    self.root.extend(items)

  def insert(self, index: int, item: ContainedT) -> None:
    if isinstance(item, (ConfiguredBaseModel, ConfiguredRootModel)):
      item._top = self._top
      item._propogate_top()
    self.root.insert(index, item)

  def index(self, item: ContainedT) -> int:
    return self.root.index(item)

  def remove(self, item: ContainedT) -> None:
    self.root.remove(item)

  def count(self, item: ContainedT) -> int:
    return self.root.count(item)

  def clear(self) -> None:
    self.root.clear()

  def __contains__(self, item: ContainedT) -> bool:
    return self.root.__contains__(item)

  def pop(self, index: int = -1) -> ContainedT:
    return self.root.pop(index)

  def __add__(self, other: Iterable[ContainedT]) -> ConfiguredListModel[ContainedT]:
    self.extend(other)
    return self

  def __iadd__(self, other: Iterable[ContainedT]) -> ConfiguredListModel[ContainedT]:
    self.extend(other)
    return self
