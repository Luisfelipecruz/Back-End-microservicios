from sqlalchemy import Column, Integer, String, Float
from database import Base


class Lugar(Base):
    __tablename__ = 'Lugar'
    idLugar = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50))
    latitude = Column(Float)
    longitude = Column(Float)
