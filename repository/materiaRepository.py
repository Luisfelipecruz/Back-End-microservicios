from models import materiaModel
from sqlalchemy.orm import Session


def listar_materias(db: Session):
    materias = db.query(materiaModel.Materia).all()
    return materias
