from abc import ABC, abstractmethod
from typing import Type, List

from Schemas.BaseSchema import BaseSchema
from Services.BaseService import BaseService


class BaseController(ABC):
    """
    Abstract base controller class.
    """

    @property
    @abstractmethod
    def service(self) -> BaseService:
        """
        Service to access database
        """

    @property
    @abstractmethod
    def schema(self) -> Type[BaseSchema]:
        """
        Pydantic Schema to validate data
        """

    @abstractmethod
    def get_all(self) -> List[BaseSchema]:
        """
        Get all data
        """

    @abstractmethod
    def get_one(self, id: int) -> BaseSchema:
        """
        Get one data
        """

    @abstractmethod
    def save(self, schema: BaseSchema) -> BaseSchema:
        """
        Save data
        """

    @abstractmethod
    def update(self, id: int, schema: BaseSchema) -> BaseSchema:
        """
        Update data
        """

    @abstractmethod
    def delete(self, id: int) -> None:
        """
        Delete data
        """