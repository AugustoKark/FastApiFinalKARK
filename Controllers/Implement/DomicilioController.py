from Controllers.BaseControllerImpl import BaseControllerImpl
from Schemas.Implement.DomicilioSchema import DomicilioSchema
from Services.Implement.DomicilioService import DomicilioService


class DomicilioController(BaseControllerImpl):
    def __init__(self):
        super().__init__(DomicilioSchema, DomicilioService())