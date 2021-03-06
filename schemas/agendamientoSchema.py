from pydantic import BaseModel
from typing import Optional
from datetime import date


class Agendamiento(BaseModel):
    idAgend: Optional[int] = None
    idHorMatGrp: int
    idUsuario: int
    Asistira: Optional[bool] = None
    fecHorReg: Optional[date] = None

    class Config:
        orm_mode = True


class AgendamientoSemanaMateria(BaseModel):
    idAgend: Optional[int] = None
    primNomUsr: Optional[str] = None
    segNomUsr: Optional[str] = None
    primApeUsr: Optional[str] = None
    DiaSemana: Optional[str] = None
    Horario: Optional[str] = None
    Salon: Optional[str] = None
    Edificio: Optional[str] = None
    Profesor: Optional[str] = None

    class Config:
        orm_mode = True

class AgendamientoSemanaMateriaUsuario(BaseModel):
    idAgend: Optional[int] = None
    nombre: Optional[str] = None
    Grupo: Optional[str] = None
    DiaSemana: Optional[str] = None
    Horario: Optional[str] = None
    Salon: Optional[str] = None
    Edificio: Optional[str] = None
    Profesor: Optional[str] = None

    class Config:
        orm_mode = True
