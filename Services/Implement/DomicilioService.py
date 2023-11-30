from Models.Implement.Domicilio import Domicilio
from Repositories.Implement.DomicilioRepository import DomicilioRepository
from Schemas.Implement.DomicilioSchema import DomicilioSchema
from Services.BaseServiceImpl import BaseServiceImpl




class DomicilioService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=DomicilioRepository(), model=Domicilio, schema=DomicilioSchema)