from Controllers.BaseControllerImpl import BaseControllerImpl
from Schemas.Implement.LocalidadSchema import LocalidadSchema
from Services.Implement.LocalidadService import LocalidadService


class LocalidadController(BaseControllerImpl):
    def __init__(self):
        super().__init__(LocalidadSchema, LocalidadService())