from Models.Implement.Libro import Libro
from Repositories.BaseRepositoryImpl import BaseRepositoryImpl
from Schemas.Implement.LibroSchema import LibroSchema


class LibroRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Libro, LibroSchema)