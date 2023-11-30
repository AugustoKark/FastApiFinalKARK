from typing import Optional

from Schemas import BaseSchema


class PersonaSchema(BaseSchema):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    dni: Optional[int] = None
    fk_domicilio: Optional[int] = None
