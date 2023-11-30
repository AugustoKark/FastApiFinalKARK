from Controllers.BaseControllerImpl import BaseControllerImpl
from Schemas.Implement.LibroSchema import LibroSchema
from Services.Implement.LibroService import LibroService


class LibroController(BaseControllerImpl):
    def __init__(self):
        super().__init__(LibroSchema, LibroService())