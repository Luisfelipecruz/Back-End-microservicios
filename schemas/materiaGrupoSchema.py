from pydantic import BaseModel
from typing import Optional


class MateriaGrupo(BaseModel):
    idMatGrp: Optional[int] = None
    idMat: int
    Capacidad: Optional[int] = None
    Matriculados: Optional[int] = None
    Grupo: Optional[str] = None

    class Config:
        orm_mode = True
