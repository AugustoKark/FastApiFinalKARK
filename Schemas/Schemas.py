from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from datetime import date

from Schemas.BaseSchema import BaseSchema


from Schemas.BaseSchema import BaseSchema

class PaymentType(Enum):
    CASH = "cash"
    CARD = "card"

class AutorSchema(BaseSchema):
    nombre: Optional[str] = None
    libros: List['LibroSchema'] = []

class LibroSchema(BaseSchema):
    
    titulo: Optional[str] = None
    autor_id: Optional[int] = None
    genero_id: Optional[int] = None
    editorial_id: Optional[int] = None
    

class GeneroSchema(BaseSchema):
    nombre: Optional[str] = None
    libros: List[LibroSchema] = []

class EditorialSchema(BaseSchema):
    nombre: Optional[str] = None
    libros: List[LibroSchema] = []

class UsuarioSchema(BaseSchema):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
   
    prestamos: List['PrestamoSchema'] = []

class PrestamoSchema(BaseSchema):
    usuario_id: Optional[int] = None
    libro_id: Optional[int]= None
    fecha_prestamo: Optional[str] = None
    

AutorSchema.model_rebuild()
LibroSchema.model_rebuild()
GeneroSchema.model_rebuild()
EditorialSchema.model_rebuild()
UsuarioSchema.model_rebuild()
PrestamoSchema.model_rebuild()