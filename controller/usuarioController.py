from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from repository import usuarioRepository
from schemas import usuarioSchema

router = APIRouter(

        prefix="/usuarios",
        tags=['Usuarios']

)

'''
Con estas lineas se crea el modelo de Usuarios en la base de datos
#from models import usuarioModel
from database import engine
usuarioModel.Base.metadata.create_all(bind=engine)
'''


@router.get("/", response_model=List[usuarioSchema.Usuario])
async def listar_todos(db: Session = Depends(get_db)):
    return usuarioRepository.listar_usuarios(db)


@router.get('/buscarUsuario', status_code=status.HTTP_200_OK, response_model=usuarioSchema.Usuario)
async def buscar_usuario_por_id(idUsuario: int, db: Session = Depends(get_db)):
    return usuarioRepository.bucar_usuario(idUsuario, db)


@router.post('/bucarMateriasEstudiante', status_code=status.HTTP_200_OK,
            response_model=List[usuarioSchema.MostrarMateriasUsuario])
async def buscar_materiaEstudiante_por_codigo(request: usuarioSchema.codigoUsuario, db: Session = Depends(get_db)):
    return usuarioRepository.bucar_materiaEstudiante_codigo(request, db)


@router.post('/bucarMateriasEstudianteHorario', status_code=status.HTTP_200_OK)
async def buscar_materiaEstudianteHorario_por_codigo(request: usuarioSchema.codigoUsuario, db: Session = Depends(get_db)):
    return usuarioRepository.bucar_materiaEstudianteHorario_codigo(request, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def crear_usuario(request: usuarioSchema.Usuario, db: Session = Depends(get_db)):
    return usuarioRepository.crear_usuario(request, db)


@router.post('/singIn', status_code=status.HTTP_201_CREATED, response_model=usuarioSchema.singInRespuesta)
async def crear_usuario(request: usuarioSchema.singInCaptura, db: Session = Depends(get_db)):
    return usuarioRepository.loguearUsuario(request, db)


@router.put('/', status_code=status.HTTP_202_ACCEPTED, response_model=usuarioSchema.Usuario)
async def actualizar_usuario(idUsuario: int, request: usuarioSchema.Usuario, db: Session = Depends(get_db)):
    return usuarioRepository.modificar_usuario(idUsuario, request, db)


@router.delete('/', status_code=status.HTTP_200_OK)
async def borrar_usuario(idUsuario: int, db: Session = Depends(get_db)):
    return usuarioRepository.eliminar_usuario(idUsuario, db)
