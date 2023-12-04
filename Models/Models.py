from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime, date
from Models.BaseModel import BaseModel

class Autor(BaseModel):
    __tablename__ = 'autores'
    
    nombre = Column(String, index=True)
    

    libros = relationship('Libro', back_populates='autor')
    

class Libro(BaseModel):
    __tablename__ = 'libros'
    
    titulo = Column(String, index=True)
    autor_id = Column(Integer, ForeignKey('autores.id'))
    genero_id = Column(Integer, ForeignKey('generos.id'))
    editorial_id = Column(Integer, ForeignKey('editoriales.id'))

    genero = relationship('Genero', back_populates='libros')
    autor = relationship('Autor', back_populates='libros')
    editorial = relationship('Editorial', back_populates='libros')
    prestamos = relationship('Prestamo', back_populates='libro')

class Genero(BaseModel):
    __tablename__ = 'generos'
    
    nombre = Column(String, index=True)
    libros = relationship('Libro', back_populates='genero')

class Editorial(BaseModel):
    __tablename__ = 'editoriales'
    
    nombre = Column(String, index=True)
    libros = relationship('Libro', back_populates='editorial')

class Usuario(BaseModel):
    __tablename__ = 'usuarios'
    
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    prestamos = relationship('Prestamo', back_populates='usuario')

class Prestamo(BaseModel):
    __tablename__ = 'prestamos'
    
    fecha_prestamo = Column(String, index=True)

    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship('Usuario', back_populates='prestamos')

    libro_id = Column(Integer, ForeignKey('libros.id'))
    libro = relationship('Libro', back_populates='prestamos')
