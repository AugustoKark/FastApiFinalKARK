from abc import ABC, abstractmethod
from typing import Type, List

from Models.BaseModel import BaseModel
from Schemas.BaseSchema import BaseSchema
from sqlalchemy.orm import Session

class BaseRepository(ABC):
    """
    BaseRepository is an abstract class that defines the methods
    that must be implemented by the repositories.
    """
    @property
    @abstractmethod
    def session(self) -> Session:
        """
        SQLAlchemy session
        """

    @property
    @abstractmethod
    def model(self) -> Type[BaseModel]:
        """
        SQLAlchemy model
        """

    @property
    @abstractmethod
    def schema(self) -> Type[BaseSchema]:
        """
        Pydantic schema
        """

    @abstractmethod
    def find(self, id: int) -> BaseSchema:
        """
        Find a record by id
        :param id: int
        :return: BaseSchema
        """

    @abstractmethod
    def find_all(self) -> List[BaseSchema]:
        """
        Find all records
        :return: List[BaseSchema]
        """

    @abstractmethod
    def save(self, model: BaseModel) -> BaseSchema:
        """
        Save a record
        :param model: BaseModel
        :return: BaseSchema
        """

    @abstractmethod
    def update(self, id: int, model: BaseModel) -> BaseSchema:
        """
        Update a record
        :param id: int
        :param model: BaseModel
        :return: BaseSchema
        """

    @abstractmethod
    def remove(self, id: int) -> None:
        """
        Delete a record by id
        :param id: int
        """

    @abstractmethod
    def save_all(self, models: List[BaseModel]) -> List[BaseSchema]:
        """
        Save multiple records
        :param models: List[BaseModel]
        :return: List[BaseSchema]
        """