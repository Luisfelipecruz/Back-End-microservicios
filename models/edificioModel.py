from sqlalchemy import Column, Integer, String, Float
from database import Base


class Edificio(Base):
    __tablename__ = 'Edificio'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idEdificio = Column(Integer)
    nombre = Column(String(40))
    NodoEntrada = Column(Integer)
