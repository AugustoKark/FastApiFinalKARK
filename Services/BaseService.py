from abc import ABC, abstractmethod
from typing import Type, List

from Models.BaseModel import BaseModel
from Repositories.BaseRepository import BaseRepository
from Schemas.BaseSchema import BaseSchema


class BaseService(ABC):
    repository: BaseRepository
    schema: Type[BaseSchema]

    @abstractmethod
    def get_all(self) -> List[BaseSchema]:
        pass

    @abstractmethod
    def get_one(self, id: int) -> BaseSchema:
        pass

    @abstractmethod
    def save(self, schema: BaseSchema) -> BaseSchema:
        pass

    @abstractmethod
    def update(self, id: int, schema: BaseSchema) -> BaseSchema:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def to_model(self, schema: BaseSchema) -> BaseModel:
        pass