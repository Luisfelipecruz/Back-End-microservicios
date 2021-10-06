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
    idMat: Optional[int] = None
    nombre: Optional[str] = None
    Grupo: Optional[str] = None

    class Config:
        orm_mode = True


class singInCaptura(BaseModel):
    usuario: Optional[int] = None
    pasword: Optional[int] = None

    class Config:
        orm_mode = True


class singInRespuesta(BaseModel):
    idUsuario: Optional[int] = None
    idRol: Optional[int] = None
    CodEst: Optional[int] = None
    primNomUsr: Optional[str] = None
    segNomUsr: Optional[str] = None
    primApeUsr: Optional[str] = None
    SegmApeUsr: Optional[str] = None
    generoUsr: Optional[str] = None
    respuesta: Optional[str] = None

    class Config:
        orm_mode = True


class codigoUsuario(BaseModel):
    CodEst: Optional[int] = None

    class Config:
        orm_mode = True


class identificadorUsuario(BaseModel):
    idUsuario: Optional[int] = None

    class Config:
        orm_mode = True