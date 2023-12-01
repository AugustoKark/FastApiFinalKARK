import logging
from contextlib import contextmanager
from typing import Type, List

from Database.database import Database
from Models.BaseModel import BaseModel
from Repositories.BaseRepository import BaseRepository
from Schemas.BaseSchema import BaseSchema


class InstanceNotFoundError(Exception):
    pass


def _to_dict(instance: BaseModel) -> dict:
    return {key: value for key, value in instance.__dict__.items() if key in instance.__table__.columns}


class BaseRepositoryImpl(BaseRepository):
    def __init__(self, model: Type[BaseModel], schema: Type[BaseSchema]):
        db = Database()
        self.session = db.get_session()
        self.model = model
        self.schema = schema
        self.logger = logging.getLogger(__name__)

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.session
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def _get_instance(self, id: int) -> BaseSchema:
        with self.session_scope() as session:
            instance = session.query(self.model).get(id)
            if instance:
                schema = self.schema.model_validate(instance)
        if instance is None:
            self.logger.error(f"No {self.model.__name__} instance found with id {id}")
            raise InstanceNotFoundError(f"No {self.model.__name__} instance found with id {id}")
        return schema

    def find_all(self) -> List[BaseSchema]:
        with self.session_scope() as session:
            instances = session.query(self.model).all()
            if instances:
                schemas = [self.schema.model_validate(instance) for instance in instances]

        return schemas

    def find_by_id(self, id: int) -> BaseSchema:

        return self._get_instance(id)

    def save(self, model: BaseModel) -> BaseSchema:
        with self.session_scope() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            schema = self.schema.model_validate(model)
        return schema

    def update(self, id: int, model: BaseModel) -> dict:
        with self.session_scope() as session:
            instance = self._get_instance(id)
            instance.update(model.__dict__)
            session.merge(instance)
            session.commit()
        return instance

    def delete(self, id: int) -> None:
        with self.session_scope() as session:
            instance = session.query(self.model).get(id)
            session.delete(instance)
            session.commit()