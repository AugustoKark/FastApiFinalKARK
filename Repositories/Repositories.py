from Models.Models import *
from Repositories.BaseRepositoryImpl import BaseRepositoryImpl
from Schemas.Schemas import *

class AutorRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Autor, AutorSchema)

class LibroRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Libro, LibroSchema)

class GeneroRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Genero, GeneroSchema)

class EditorialRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Editorial, EditorialSchema)

class UsuarioRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Usuario, UsuarioSchema)

class PrestamoRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(Prestamo, PrestamoSchema)
    

