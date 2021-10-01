from pydantic import BaseModel
from typing import Optional


class MateriaEstudiante(BaseModel):
    id: Optional[int] = None
    IdMat: Optional[int] = None
    Grupo: Optional[str] = None
    idUsr: Optional[str] = None
    codEst: Optional[int] = None
    primNomUsr: Optional[str] = None
    segNomUsr: Optional[str] = None
    primApeUsr: Optional[str] = None
    segApeUsr: Optional[str] = None
    generoUsr: Optional[str] = None

    class Config:
        orm_mode = True