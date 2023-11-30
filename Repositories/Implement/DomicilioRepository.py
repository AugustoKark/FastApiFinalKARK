from Models.Implement.Domicilio import Domicilio
from Repositories.BaseRepositoryImpl import BaseRepositoryImpl


class DomicilioRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Domicilio)