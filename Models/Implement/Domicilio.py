from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Models.BaseModel import BaseModel


class Domicilio(BaseModel):
    __tablename__ = 'Domicilio'

    calle = Column(String)
    numero = Column(Integer)
    fk_localidad = Column(Integer, ForeignKey('Localidad.id'))

    persona = relationship("Persona", back_populates="domicilio")
    localidad = relationship("Localidad", back_populates="domicilios")


    # def __init__(self, calle, numero, fk_localidad):
    #     self.calle = calle
    #     self.numero = numero
    #     self.fk_localidad = fk_localidad