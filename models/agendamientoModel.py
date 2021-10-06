from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from database import Base


class Agendamiento(Base):
    __tablename__ = 'Agendamiento'
    idAgend = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idAgend = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idHorMatGrp = Column(Integer, ForeignKey('HorarioMateriaGrupo.idHorMatGrp'))
    idUsuario = Column(Integer, ForeignKey('Usuario.idUsuario'))
    Asistira = Column(Boolean)
    fecHorReg = Column(Date)
