from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class MateriaGrupo(Base):
    __tablename__ = 'MateriaGrupo'
    idMatGrp = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idMat = Column(Integer, ForeignKey('Materia.idMat'))
    Capacidad = Column(Integer)
    Matriculados = Column(Integer)
    Grupo = Column(String(6))
