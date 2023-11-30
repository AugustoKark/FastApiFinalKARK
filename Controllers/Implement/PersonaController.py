from Controllers.BaseControllerImpl import BaseControllerImpl
from schemas.address_schema import AddressSchema
from services.address_service import AddressService


class PersonaController(BaseControllerImpl):
    def __init__(self):
        super().__init__(PersonaSchema, PersonaService())