from pydantic import BaseModel
from typing import Optional


class Lugar(BaseModel):
    idLugar: Optional[int] = None
    nombre: Optional[str] = None
    latitude: float
    longitude: float

    class Config:
        orm_mode = True
