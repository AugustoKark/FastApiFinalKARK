from Controllers.BaseControllerImpl import BaseControllerImpl
from Schemas.Implement.AutorSchema import AutorSchema
from Services.Implement.AutorService import AutorService


class AutorController(BaseControllerImpl):
    def __init__(self):
        super().__init__(AutorSchema, AutorService())