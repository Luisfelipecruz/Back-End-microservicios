from pydantic import BaseModel
from typing import Optional


class Rol(BaseModel):
    idRol: Optional[int] = None
    nombre: Optional[str] = None

    class Config:
        orm_mode = True
