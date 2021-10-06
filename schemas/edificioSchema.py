from pydantic import BaseModel
from typing import Optional


class Edificio(BaseModel):
    id: Optional[int] = None
    idEdificio: Optional[int] = None
    nombreEdificio: Optional[str] = None
    nodoEntrada: Optional[int] = None

    class Config:
        orm_mode = True
