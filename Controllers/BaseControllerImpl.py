from typing import Type, List

from fastapi import APIRouter, HTTPException

from Controllers.BaseController import BaseController
from Schemas.BaseSchema import BaseSchema
from Services.BaseServiceImpl import BaseServiceImpl




class BaseControllerImpl(BaseController):
    def __init__(self, schema: Type[BaseSchema], service: BaseServiceImpl):
        self.schema = schema
        self.service = service
        self.router = APIRouter()

        @self.router.get("/", response_model=List[self.schema])
        def get_all():
            return self.get_all()

        @self.router.get("/{id}", response_model=self.schema)
        def get_one(id: int):
            item = self.get_one(id)
            if item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return item

        @self.router.post("/", response_model=self.schema)
        def save(schema_in: schema):
            return self.save(schema_in)

        @self.router.put("/{id}", response_model=self.schema)
        def update(id: int, schema_in: schema):
            item = self.update(id, schema_in)
            if item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return item

        @self.router.delete("/{id}")
        def delete(id: int):
            self.delete(id)

    def get_all(self):
        return self.service.get_all()

    def get_one(self, id: int):
        return self.service.get_one(id)

    def save(self, schema: BaseSchema):
        return self.service.save(schema)

    def update(self, id: int, schema: BaseSchema):
        return self.service.update(id, schema)

    def delete(self, id: int):
        self.service.delete(id)