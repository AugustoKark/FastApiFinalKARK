from Models.Implement.Localidad import Localidad
from Repositories.BaseRepositoryImpl import BaseRepositoryImpl
from Schemas.Implement.LocalidadSchema import LocalidadSchema


class LocalidadRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Localidad, LocalidadSchema)