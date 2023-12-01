from abc import ABC, abstractmethod
from typing import Type, List

from Models.BaseModel import BaseModel
from Schemas.BaseSchema import BaseSchema


class BaseRepository(ABC):
    model: Type[BaseModel]

    @abstractmethod
    def find_all(self) -> List[BaseSchema]:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> BaseSchema:
        pass

    @abstractmethod
    def save(self, model: BaseModel) -> BaseSchema:
        pass

    @abstractmethod
    def update(self, id: int, model: BaseModel) -> BaseSchema:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass