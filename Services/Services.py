from Models.Models import *
from Repositories.Repositories import *
from Schemas.Schemas import *
from Services.BaseServiceImpl import BaseServiceImpl

class AutorService(BaseServiceImpl):
    def __init__(self):
        super().__init__(repository=AutorRepository(),model= Autor, schema=AutorSchema)

class LibroService(BaseServiceImpl):
    def __init__(self):
        super().__init__(repository=LibroRepository(),model= Libro, schema=LibroSchema)

class GeneroService(BaseServiceImpl):
    def __init__(self):
        super().__init__(repository=GeneroRepository(),model= Genero, schema=GeneroSchema)

class EditorialService(BaseServiceImpl):
    def __init__(self):
        super().__init__(repository=EditorialRepository(),model= Editorial, schema=EditorialSchema)
    
class UsuarioService(BaseServiceImpl):
    def __init__(self):
        super().__init__(repository=UsuarioRepository(),model= Usuario, schema=UsuarioSchema)

class PrestamoService(BaseServiceImpl):
    def __init__(self):
        super().__init__(repository=PrestamoRepository(),model= Prestamo, schema=PrestamoSchema)

