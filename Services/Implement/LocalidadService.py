from Models.Implement.Localidad import Localidad
from Repositories.Implement.LocalidadRepository import LocalidadRepository
from Schemas.Implement.LocalidadSchema import LocalidadSchema
from Services.BaseServiceImpl import BaseServiceImpl




class LocalidadService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=LocalidadRepository(), model=Localidad, schema=LocalidadSchema)