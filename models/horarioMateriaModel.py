from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class HorarioMateriaGrupo(Base):
    __tablename__ = 'HorarioMateriaGrupo'
    idHorMatGrp = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idMatGrp = Column(Integer, ForeignKey('MateriaGrupo.idMatGrp'))
    idLugar = Column(Integer, ForeignKey('Lugar.idLugar'))
    Salon = Column(String(15))
    Edificio = Column(String(25))
    DiaSemana = Column(String(15))
    Horario = Column(String(10))
    Profesor = Column(String(45))
