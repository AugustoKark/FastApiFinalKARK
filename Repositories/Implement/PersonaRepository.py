from Models.Implement.Persona import Persona
from Repositories.BaseRepositoryImpl import BaseRepositoryImpl


class PersonaRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Persona)