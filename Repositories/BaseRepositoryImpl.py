import logging
from contextlib import contextmanager
from typing import Type, List

from Database.database import Database
from Models.BaseModel import BaseModel
from Repositories.BaseRepository import BaseRepository
from Schemas.BaseSchema import BaseSchema
from sqlalchemy.orm import Session
from typing import TypeVar


class InstanceNotFoundError(Exception):
    """
    InstanceNotFoundError is raised when a record is not found
    """


class BaseRepositoryImpl(BaseRepository):
    """
    Class BaseRepositoryImpl implements BaseRepository
    """

    def __init__(self, model: Type[BaseModel], schema: Type[BaseSchema]):
        self._model = model
        self._schema = schema
        self.logger = logging.getLogger(__name__)
        self._session = Database().get_session()

    @property
    def session(self) -> Session:
        return self._session

    @property
    def model(self) -> Type[BaseModel]:
        return self._model

    @property
    def schema(self) -> Type[BaseSchema]:
        return self._schema

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.session
        try:
            yield session
            session.commit()
        except Exception as e:
            self.logger.error("Session rollback because of error %s", e)
            session.rollback()
            raise
        finally:
            session.close()

    def find(self, id: int) -> BaseSchema:
        with self.session_scope() as session:
            model = session.query(self.model).get(id)
            if model is None:
                raise InstanceNotFoundError(f"No instance found with id {id}")
            return self.schema.model_validate(model)

    def find_all(self) -> List[BaseSchema]:
        with self.session_scope() as session:
            models = session.query(self.model).all()
            schemas = []
            for model in models:
                schemas.append(self.schema.model_validate(model))
            return schemas

    def save(self, model: BaseModel) -> BaseSchema:
        with self.session_scope() as session:
            session.add(model)
            return self.schema.model_validate(model)

    def update(self, id: int, model: BaseModel) -> BaseSchema:
        with self.session_scope() as session:
            instance = session.query(self.model).get(id)
            if instance:
                for key, value in model.__dict__.items():
                    setattr(instance, key, value)

                print(instance)
                session.commit()
                # Asegúrate de que la instancia esté en el contexto de la sesión
                session.add(instance)
                session.refresh(instance)  # Debe ejecutarse después del commit
                return instance
            return None

    def remove(self, id: int) -> None:
        with self.session_scope() as session:
            model = session.query(self.model).get(id)
            if model is None:
                raise InstanceNotFoundError(f"No instance found with id {id}")
            session.delete(model)

    def save_all(self, models: List[BaseModel]) -> List[BaseSchema]:
        with self.session_scope() as session:
            session.add_all(models)