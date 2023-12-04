from typing import Type, List

from fastapi import APIRouter, HTTPException

from Controllers.BaseController import BaseController
from Schemas.BaseSchema import BaseSchema
from Services.BaseService import BaseService


class BaseControllerImpl(BaseController):
    """Base controller implementation."""

    def __init__(self, schema: Type[BaseSchema], service: BaseService,):
        self.service = service
        self.schema = schema
        self.router = APIRouter()

        @self.router.get("/", response_model=List[schema])
        async def get_all():
            return self.get_all()

        @self.router.get("/{id}", response_model=schema)
        async def get_one(id: int):
            item = self.get_one(id)
            if item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return item

        @self.router.post("/", response_model=schema)
        async def save(schema_in: schema):
            return self.save(schema_in)

        @self.router.put("/{id}", response_model=schema)
        async def update(id: int, schema_in: schema):
            item = self.update(id, schema_in)
            if item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return item

        @self.router.delete("/{id}")
        async def delete(id: int):
            self.delete(id)

    @property
    def service(self) -> BaseService:
        """Service to access database."""
        return self._service

    @property
    def schema(self) -> Type[BaseSchema]:
        """Pydantic Schema to validate data."""
        return self._schema

    def get_all(self) -> List[BaseSchema]:
        """Get all data."""
        return self.service.get_all()

    def get_one(self, id: int) -> BaseSchema:
        """Get one data."""
        return self.service.get_one(id)

    def save(self, schema: BaseSchema) -> BaseSchema:
        """Save data."""
        return self.service.save(schema)

    def update(self, id: int, schema: BaseSchema) -> BaseSchema:
        """Update data."""
        return self.service.update(id, schema)

    def delete(self, id: int) -> None:
        """Delete data."""
        self.service.delete(id)

    @schema.setter
    def schema(self, value):
        self._schema = value

    @service.setter
    def service(self, value):
        self._service = value