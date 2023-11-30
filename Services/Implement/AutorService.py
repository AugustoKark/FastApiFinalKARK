
from Models.Implement.Autor import Autor
from Repositories.Implement.AutorRepository import AutorRepository
from Schemas.Implement.AutorSchema import AutorSchema
from Services.BaseServiceImpl import BaseServiceImpl




class AutorService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=AutorRepository(), model=Autor, schema=AutorSchema)