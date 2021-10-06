from sqlalchemy import Column, Integer, ForeignKey
from database import Base


class MateriaEstudiante(Base):
    __tablename__ = 'MateriaEstudiante'
    idMatEst = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idMat = Column(Integer, ForeignKey('Materia.idMat'))
    idUsuario = Column(Integer, ForeignKey('Usuario.idUsuario'))
    idMatGrp = Column(Integer, ForeignKey('MateriaGrupo.idMatGrp'))
