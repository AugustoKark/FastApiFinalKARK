from Models.Implement.Libro import Libro
from Repositories.Implement.LibroRepository import LibroRepository
from Schemas.Implement.LibroSchema import LibroSchema
from Services.BaseServiceImpl import BaseServiceImpl




class LibroService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=LibroRepository(), model=Libro, schema=LibroSchema)