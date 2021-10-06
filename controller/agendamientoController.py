from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from repository import agendamientoRepository
from schemas import agendamientoSchema, usuarioSchema

router = APIRouter(

        prefix="/agendamiento",
        tags=['Agendamiento']

)

'''
Con estas lineas se crea el modelo de Usuarios en la base de datos
#from models import agendamientoModel
from database import engine
agendamientoModel.Base.metadata.create_all(bind=engine)
'''


@router.get("/", response_model=List[agendamientoSchema.Agendamiento])
async def listar_reservas(db: Session = Depends(get_db)):
    return agendamientoRepository.listar_reservas(db)


@router.get('/ReservasSemanaTodos', status_code=status.HTTP_200_OK,
            response_model=List[agendamientoSchema.Agendamiento])
async def buscar_reservas_Semana_Todos(db: Session = Depends(get_db)):
    return agendamientoRepository.bucar_reserva_semana_todos(db)


@router.post('/ReservasSemanaUsuario', status_code=status.HTTP_200_OK,
            response_model=List[agendamientoSchema.AgendamientoSemanaMateriaUsuario])
async def buscar_reservas_Semana_Usuario(request: usuarioSchema.identificadorUsuario, db: Session = Depends(get_db)):
    return agendamientoRepository.bucar_reserva_semana_usuarios(request, db)


@router.get('/ReservasSemanaMateria', status_code=status.HTTP_200_OK,
            response_model=List[agendamientoSchema.AgendamientoSemanaMateria])
async def buscar_reservas_Semana_Materia(idMat: int, db: Session = Depends(get_db)):
    return agendamientoRepository.buscar_reservas_Semana_Materia(idMat, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def crear_reserva(request: agendamientoSchema.Agendamiento, db: Session = Depends(get_db)):
    return agendamientoRepository.crear_reserva(request, db)


@router.put('/', status_code=status.HTTP_202_ACCEPTED, response_model=agendamientoSchema.Agendamiento)
async def actualizar_reserva(request: agendamientoSchema.Agendamiento, db: Session = Depends(get_db)):
    return agendamientoRepository.modificar_reserva(request, db)
