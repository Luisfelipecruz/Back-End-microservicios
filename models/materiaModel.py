from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Materia(Base):
    __tablename__ = 'Materia'
    idMat = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50))
