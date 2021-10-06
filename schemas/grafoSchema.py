from pydantic import BaseModel
from typing import List, Optional


class Grafo(BaseModel):
    Pnt_inicial: Optional[str] = None
    Pnt_final: Optional[str] = None
    Respuesta: List[str] = []

    class Config:
        orm_mode = True