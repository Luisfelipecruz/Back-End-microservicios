from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from repository import grafoRepository
from schemas import grafoSchema

router = APIRouter(

        prefix="/grafoUIS",
        tags=['GrafoUIS']

)


@router.post('/bucarMateriasEstudiante', status_code=status.HTTP_200_OK)
async def buscar_materiaEstudiante_por_codigo(request: grafoSchema.Grafo):
    return grafoRepository.bucar_camino_mas_corto(request)
