from Controllers.BaseControllerImpl import BaseControllerImpl
from Schemas.Implement.PersonaSchema import PersonaSchema
from Services.Implement.PersonaService import PersonaService


class PersonaController(BaseControllerImpl):
    def __init__(self):
        super().__init__(PersonaSchema, PersonaService())