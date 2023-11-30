from abc import ABC, abstractmethod
from typing import Type, List

from Models.BaseModel import BaseModel


class BaseRepository(ABC):
    model: Type[BaseModel]

    @abstractmethod
    def find_all(self) -> List[dict]:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> dict:
        pass

    @abstractmethod
    def save(self, model: BaseModel) -> dict:
        pass

    @abstractmethod
    def update(self, id: int, model: BaseModel) -> dict:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass