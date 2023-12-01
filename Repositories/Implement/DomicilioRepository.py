from Models.Implement.Domicilio import Domicilio
from Repositories.BaseRepositoryImpl import BaseRepositoryImpl
from Schemas.Implement.DomicilioSchema import DomicilioSchema


class DomicilioRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Domicilio, DomicilioSchema)