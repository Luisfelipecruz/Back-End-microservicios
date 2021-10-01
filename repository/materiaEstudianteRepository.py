from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas import materiaEstudianteSchema
from models import materiaEstudianteModel


def listar_materiaEstudiante(db: Session):
    materiaEstudiante = db.query(materiaEstudianteModel.MateriaEstudiante).all()
    return materiaEstudiante


def bucar_materiaEstudiante_id(_id: int, db: Session):
    materiaEstudiante = db.query(materiaEstudianteModel.MateriaEstudiante).filter(
            materiaEstudianteModel.MateriaEstudiante.id == _id).first()
    if not materiaEstudiante:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El registro con de materia estudiante con id {_id} no esta disponible")
    return materiaEstudiante


def bucar_materiaEstudiante_codigo(codigo: int, db: Session):
    materiasEstudiante = db.query(materiaEstudianteModel.MateriaEstudiante).filter(
            materiaEstudianteModel.MateriaEstudiante.codEst == codigo).all()
    if not materiasEstudiante:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No hay registro con el codigo de estudiante {codigo} ")
    return materiasEstudiante
