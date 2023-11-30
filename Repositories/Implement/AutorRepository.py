from Models.Implement.Autor import Autor
from Repositories.BaseRepositoryImpl import BaseRepositoryImpl


class AutorRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Autor)