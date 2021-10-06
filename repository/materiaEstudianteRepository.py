from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import materiaEstudianteModel, usuarioModel
from schemas import usuarioSchema


def listar_materiaEstudiante(db: Session):
    materiaEstudiante = db.query(materiaEstudianteModel.MateriaEstudiante).all()
    return materiaEstudiante


def bucar_materiaEstudiante_id(request: usuarioSchema.codigoUsuario, db: Session):
    CODIGO = request.CodEst
    materiaEstudiante = db.query(materiaEstudianteModel.MateriaEstudiante).join(usuarioModel.Usuario)\
        .filter(usuarioModel.Usuario.CodEst == CODIGO).first()
    if not materiaEstudiante:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No se tienen materias registradas para el estudiante con codigo {CODIGO}")
    return materiaEstudiante
