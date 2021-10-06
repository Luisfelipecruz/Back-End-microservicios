from pydantic import BaseModel
from typing import Optional
from datetime import date


class Agendamiento(BaseModel):
    idAgend: Optional[int] = None
    idHorMatGrp: int
    idUsuario: int
    Asistira: bool
    fecHorReg: date

    class Config:
        orm_mode = True
