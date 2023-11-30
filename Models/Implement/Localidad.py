from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from Models.BaseModel import BaseModel


class Localidad(BaseModel):
    __tablename__ = 'Localidad'

    denominacion = Column(String)

    domicilios = relationship("Domicilio", back_populates="localidad")

    # def __init__(self, denominacion):
    #     self.denominacion = denominacion

    # def __repr__(self):
    #     return f"Localidad {self.denominacion}"