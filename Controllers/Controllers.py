from Controllers.BaseControllerImpl import BaseControllerImpl
from Schemas.Schemas import *
from Services.Services import *

class AutorController(BaseControllerImpl):
    def __init__(self):
        super().__init__(AutorSchema, AutorService())

class LibroController(BaseControllerImpl):
    def __init__(self):
        super().__init__(LibroSchema, LibroService())

class GeneroController(BaseControllerImpl):
    def __init__(self):
        super().__init__(GeneroSchema, GeneroService())

class EditorialController(BaseControllerImpl):
    def __init__(self):
        super().__init__(EditorialSchema, EditorialService())

class UsuarioController(BaseControllerImpl):
    def __init__(self):
        super().__init__(UsuarioSchema, UsuarioService())

class PrestamoController(BaseControllerImpl):
    def __init__(self):
        super().__init__(PrestamoSchema, PrestamoService())

