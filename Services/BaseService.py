from abc import ABC, abstractmethod
from typing import Type, List

from Models.BaseModel import BaseModel
from Repositories.BaseRepository import BaseRepository
from Schemas.BaseSchema import BaseSchema


class BaseService(ABC):
    """Base Service"""

    @property
    @abstractmethod
    def repository(self) -> BaseRepository:
        """
        Repository to access database
        """

    @property
    @abstractmethod
    def schema(self) -> BaseSchema:
        """
        Pydantic Schema to validate data
        """

    @property
    @abstractmethod
    def model(self) -> BaseModel:
        """
        SQLAlchemy Model
        """

    @abstractmethod
    def get_all(self) -> List[BaseSchema]:
        """Get all"""

    @abstractmethod
    def get_one(self, id: int) -> BaseSchema:
        """Get by id"""

    @abstractmethod
    def save(self, schema: BaseSchema) -> BaseSchema:
        """Save"""

    @abstractmethod
    def update(self, id: int, schema: BaseSchema) -> BaseSchema:
        """Update"""

    @abstractmethod
    def delete(self, id: int) -> None:
        """Delete"""

    @abstractmethod
    def to_model(self, schema: BaseSchema) -> BaseModel:
        """To model"""