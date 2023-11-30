from sqlalchemy import Column, String
from Models.BaseModel import BaseModel

class Autor(BaseModel):
    __tablename__ = 'Autor'

    nombre = Column(String)
    apellido = Column(String)
    biografia = Column(String(length=1500))
    
    # def __init__(self, nombre, apellido, biografia):
    #     self.nombre = nombre
    #     self.apellido = apellido
    #     self.biografia = biografia