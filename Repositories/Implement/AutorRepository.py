from Models.Implement.Autor import Autor
from Repositories.BaseRepositoryImpl import BaseRepositoryImpl
from Schemas.Implement.AutorSchema import AutorSchema


class AutorRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Autor, AutorSchema)