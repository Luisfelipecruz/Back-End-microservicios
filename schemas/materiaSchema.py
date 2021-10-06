from pydantic import BaseModel
from typing import Optional


class Materia(BaseModel):
    idMat: Optional[int] = None
    nombre: Optional[str] = None

    class Config:
        orm_mode = True
