from Models.BaseModel import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table




# Asegúrate de tener la tabla persona_libro definida
persona_libro_association = Table(
    'persona_libro', BaseModel.metadata,
    Column('persona_id', Integer, ForeignKey('Persona.id')),
    Column('libro_id', Integer, ForeignKey('Libro.id'))
)

class Persona(BaseModel):
    __tablename__ = 'Persona'

    nombre = Column(String)
    apellido = Column(String)
    dni = Column(Integer)
    fk_domicilio = Column(Integer, ForeignKey('Domicilio.id'))

    domicilio = relationship("Domicilio", back_populates="persona")
    libros = relationship("Libro", secondary=persona_libro_association)



    # def __init__(self, nombre, apellido, dni):
    #     self.nombre = nombre
    #     self.apellido = apellido
    #     self.dni = dni

    # def __repr__(self):
    #     return f"Persona {self.nombre} {self.apellido} {self.dni}"