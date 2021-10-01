from sqlalchemy import Column, Integer, String
from database import Base


class MateriaEstudiante(Base):
    __tablename__ = 'MateriaEstudiante'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    IdMat = Column(Integer)
    Grupo = Column(String(6))
    idUsr = Column(String(7))
    codEst = Column(Integer)
    primNomUsr = Column(String(18))
    segNomUsr = Column(String(18))
    primApeUsr = Column(String(18))
    segApeUsr = Column(String(18))
    generoUsr = Column(String(11))
