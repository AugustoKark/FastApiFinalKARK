from sqlalchemy import Column, String, Integer, Table, ForeignKey
from Models.BaseModel import BaseModel

from sqlalchemy.orm import relationship

libro_autor_association = Table(
    'libro_autor', BaseModel.metadata,
    Column('libro_id', Integer, ForeignKey('Libro.id')),
    Column('autor_id', Integer, ForeignKey('Autor.id'))
)

class Libro(BaseModel):
    __tablename__ = 'Libro'

    titulo = Column(String)
    fecha = Column(Integer)
    genero = Column(String)
    paginas = Column(Integer)

    autores = relationship("Autor", secondary=libro_autor_association)


    # def __init__(self, titulo, fecha, genero, paginas):
    #     self.titulo = titulo
    #     self.fecha = fecha
    #     self.genero = genero
    #     self.paginas = paginas
    
    # def __repr__(self):
    #     return f"Libro {self.titulo} {self.fecha} {self.genero} {self.paginas}"