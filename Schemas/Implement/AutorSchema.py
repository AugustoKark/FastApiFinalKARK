from typing import Optional

from Schemas.BaseSchema import BaseSchema


class AutorSchema(BaseSchema):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    biografia: Optional[str] = None
