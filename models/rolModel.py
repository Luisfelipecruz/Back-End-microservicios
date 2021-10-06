from sqlalchemy import Column, Integer, String
from database import Base


class Rol(Base):
    __tablename__ = 'Rol'
    idRol = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(30))
