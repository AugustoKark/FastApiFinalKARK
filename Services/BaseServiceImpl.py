from typing import Type, List


from Services.BaseService import BaseService

from Models.BaseModel import BaseModel
from Repositories.BaseRepository import BaseRepository
from Schemas.BaseSchema import BaseSchema



class BaseServiceImpl(BaseService):
    """ Base Service Implementation"""
    def __init__(self, repository: BaseRepository,
                 model: Type[BaseModel],
                 schema: Type[BaseSchema]):
        self.repository = repository
        self.model = model
        self.schema = schema

    @property
    def repository(self) -> BaseRepository:
        """Repository to access database"""
        return self._repository

    @property
    def schema(self) -> BaseSchema:
        """Pydantic Schema to validate data"""
        return self._schema

    @property
    def model(self) -> BaseModel:
        """SQLAlchemy Model"""
        return self._model

    def get_all(self) -> List[BaseSchema]:
        """Get all data"""
        return self.repository.find_all()

    def get_one(self, id: int) -> BaseSchema:
        """Get one data"""
        return self.repository.find(id)

    def save(self, schema: BaseSchema) -> BaseSchema:
        """Save data"""
        return self.repository.save(self.to_model(schema))

    def update(self, id: int, schema: BaseSchema) -> BaseSchema:
        """Update data"""
        return self.repository.update(id, schema.model_dump())

    def delete(self, id: int) -> None:
        """Delete data"""
        self.repository.remove(id)

    def to_model(self, schema: BaseSchema) -> BaseModel:
        model_class = type(self.model) if not callable(self.model) else self.model
        model_instance = model_class(**schema.model_dump())
        return model_instance

    @repository.setter
    def repository(self, value):
        self._repository = value

    @model.setter
    def model(self, value):
        self._model = value

    @schema.setter
    def schema(self, value):
        self._schema = value