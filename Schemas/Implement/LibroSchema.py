from typing import Optional

from Schemas import BaseSchema


class LibroSchema(BaseSchema):
    titulo: Optional[str] = None
    fecha: Optional[int] = None
    genero : Optional[str] = None
    paginas : Optional[int] = None
