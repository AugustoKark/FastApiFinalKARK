from Models.Implement.Localidad import Localidad
from Repositories.BaseRepositoryImpl import BaseRepositoryImpl


class LocalidadRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Localidad)