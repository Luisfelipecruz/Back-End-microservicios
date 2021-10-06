from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Usuario(Base):
    __tablename__ = 'Usuario'
    idUsuario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idRol = Column(Integer, ForeignKey('Rol.idRol'))
    CodEst = Column(Integer)
    email = Column(String(30))
    primNomUsr = Column(String(20))
    segNomUsr = Column(String(20))
    primApeUsr = Column(String(20))
    SegmApeUsr = Column(String(20))
    generoUsr = Column(String(12))
