from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from repository import grafoRepository
from schemas import grafoSchema
from schemas import edificioSchema

router = APIRouter(

        prefix="/grafoUIS",
        tags=['GrafoUIS']

)


@router.post('/grafoCaminoMasCorto', status_code=status.HTTP_200_OK)
async def buscar_materiaEstudiante_por_codigo(request: grafoSchema.Grafo):
    return grafoRepository.bucar_camino_mas_corto(request)


@router.get('/listarEdificios', response_model=List[edificioSchema.Edificio], status_code=status.HTTP_200_OK)
async def listarEdificios(db: Session = Depends(get_db)):
    return grafoRepository.listarALLedificios(db)
