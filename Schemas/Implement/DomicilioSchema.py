from typing import Optional

from Schemas import BaseSchema


class DomicilioSchema(BaseSchema):
    calle: Optional[str] = None
    numero: Optional[int] = None
    fk_localidad: Optional[str] = None
    
