from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from repository import materiaEstudianteRepository
from schemas import materiaEstudianteSchema

router = APIRouter(

        prefix="/materiaEstudiante",
        tags=['MateriaEstudiante']

)

'''
Con estas lineas se crea el modelo de materiaEstudiante en la base de datos
from models import materiaEstudianteModel
from database import engine
materiaEstudianteModel.Base.metadata.create_all(bind=engine)
'''


@router.get("/listarTodos", status_code=status.HTTP_200_OK, response_model=List[materiaEstudianteSchema.MateriaEstudiante])
async def listar_todos(db: Session = Depends(get_db)):
    return materiaEstudianteRepository.listar_materiaEstudiante(db)


@router.get('/bucarPorId', status_code=status.HTTP_200_OK, response_model=materiaEstudianteSchema.MateriaEstudiante)
async def buscar_materiaEstudiante_codigo(codigo: int, db: Session = Depends(get_db)):
    return materiaEstudianteRepository.bucar_materiaEstudiante_id(codigo, db)


