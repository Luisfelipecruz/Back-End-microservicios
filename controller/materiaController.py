from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from repository import materiaRepository
from schemas import materiaSchema

router = APIRouter(

        prefix="/materia",
        tags=['Materia']

)

'''
Con estas lineas se crea el modelo de Usuarios en la base de datos
#from models import materiaModel
from database import engine
materiaModel.Base.metadata.create_all(bind=engine)
'''


@router.get("/", response_model=List[materiaSchema.Usuario])
async def listar_materias(db: Session = Depends(get_db)):
    return materiaRepository.listar_materias(db)