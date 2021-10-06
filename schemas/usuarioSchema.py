from pydantic import BaseModel
from typing import Optional


class Usuario(BaseModel):
    idUsuario: Optional[int] = None
    idRol: Optional[int] = None
    CodEst: Optional[int] = None
    email: Optional[str] = None
    primNomUsr: Optional[str] = None
    segNomUsr: Optional[str] = None
    primApeUsr: Optional[str] = None
    SegmApeUsr: Optional[str] = None
    generoUsr: Optional[str] = None

    class Config:
        orm_mode = True


class MostrarMateriasUsuario(BaseModel):
    idUsuario: Optional[int] = None
    nombre: Optional[str] = None
    Grupo: Optional[str] = None

    class Config:
        orm_mode = True
