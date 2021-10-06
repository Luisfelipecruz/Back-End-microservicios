from pydantic import BaseModel
from typing import Optional


class MateriaEstudiante(BaseModel):
    idMatEst: Optional[int] = None
    idMat: int
    idUsuario: int
    idMatGrp: int

    class Config:
        orm_mode = True
