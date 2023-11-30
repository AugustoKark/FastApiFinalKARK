from Models.Implement.Persona import Persona
from Repositories.Implement.PersonaRepository import PersonaRepository
from Schemas.Implement.PersonaSchema import PersonaSchema
from Services.BaseServiceImpl import BaseServiceImpl




class PersonaService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=PersonaRepository(), model=Persona, schema=PersonaSchema)