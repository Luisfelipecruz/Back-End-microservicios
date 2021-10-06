from pydantic import BaseModel
from typing import Optional


class HorarioMateriaGrupo(BaseModel):
    idHorMatGrp: Optional[int] = None
    idMatGrp: int
    idLugar: int
    Salon: Optional[str] = None
    Edificio: Optional[str] = None
    DiaSemana: Optional[str] = None
    Horario: Optional[str] = None
    Profesor: Optional[str] = None

    class Config:
        orm_mode = True
