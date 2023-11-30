from abc import ABC, abstractmethod
from typing import Type, List

from Schemas.BaseSchema import BaseSchema
from Services.BaseService import BaseService


class BaseController(ABC):
    service: BaseService
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