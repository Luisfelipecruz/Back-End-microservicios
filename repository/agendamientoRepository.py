from datetime import timedelta, date, datetime

from fastapi import HTTPException, status
from sqlalchemy import Integer, Unicode, DateTime, String, and_, text, column
from schemas import usuarioSchema
from models import agendamientoModel
from sqlalchemy.orm import Session


def listar_reservas(db: Session):
    reservas = db.query(agendamientoModel.Agendamiento).all()
    return reservas


def bucar_reserva_semana_todos(db: Session):
    start_range = date.today() + timedelta(weeks=-1)
    end_range = date.today() + timedelta(weeks=1)

    reservas_Semana_Curso = db.query(agendamientoModel.Agendamiento).filter(
            and_(agendamientoModel.Agendamiento.Asistira == 1),
            (agendamientoModel.Agendamiento.fecHorReg.between(start_range, end_range))
    ).all()

    if not reservas_Semana_Curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Para la fecha {date.today()} no hay registros")
    return reservas_Semana_Curso


'''def bucar_reserva_semana_usuarios(ID_Usuario, db):
    start_range = date.today() + timedelta(weeks=-1)
    end_range = date.today() + timedelta(weeks=1)

    reservas_Semana_Usuario_Curso = db.query(agendamientoModel.Agendamiento).filter(
            and_(agendamientoModel.Agendamiento.Asistira == 1),
            (agendamientoModel.Agendamiento.fecHorReg.between(start_range, end_range)),
            (agendamientoModel.Agendamiento.idUsuario == ID_Usuario)
    ).all()

    if not reservas_Semana_Usuario_Curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Para la fecha {date.today()} el usuario no tiene registros")
    return reservas_Semana_Usuario_Curso'''


def bucar_reserva_semana_usuarios(request: usuarioSchema.identificadorUsuario, db: Session):
    ID_Usuario = request.idUsuario
    start_range = date.today() + timedelta(weeks=-1)
    end_range = date.today() + timedelta(weeks=1)

    agendamientoModel.Agendamiento.fecHorReg.between(start_range, end_range)
    stmt = text("SELECT Agendamiento.idAgend AS idAgend, Materia.nombre AS nombre, "
                "MateriaGrupo.Grupo AS Grupo, MateriaGrupo.Matriculados AS Matriculados, "
                "HorarioMateriaGrupo.Horario AS Horario, HorarioMateriaGrupo.Salon AS Salon, "
                "HorarioMateriaGrupo.Edificio AS Edificio, HorarioMateriaGrupo.Profesor AS Profesor "
                "FROM Agendamiento JOIN Usuario ON Usuario.idUsuario = Agendamiento.idUsuario "
                "JOIN HorarioMateriaGrupo ON Agendamiento.idHorMatGrp = HorarioMateriaGrupo.idHorMatGrp "
                "JOIN MateriaGrupo ON MateriaGrupo.idMatGrp = HorarioMateriaGrupo.idMatGrp "
                "JOIN Materia ON Materia.idMat = MateriaGrupo.idMat "
                "WHERE Usuario.idUsuario =:ID_Usuario "
                "AND Agendamiento.fecHorReg >=:start_range "
                "AND Agendamiento.fecHorReg <=:end_range "
                "AND Agendamiento.Asistira = 1 "). \
        bindparams(ID_Usuario=ID_Usuario, start_range=start_range, end_range=end_range). \
        columns(column('idAgend', Integer), column('nombre', Unicode), column('Grupo', Unicode),
                column('Matriculados', Unicode), column('Horario', Unicode), column('Salon', Unicode),
                column('Edificio', Unicode), column('Profesor', Unicode))

    result = db.execute(stmt)

    reservasSemanaMateria = [dict(row) for row in result]

    if not reservasSemanaMateria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No hay reservas en esta semana para la materia")
    return reservasSemanaMateria


def buscar_reservas_Semana_Materia(ID_MAT: int, db: Session):
    start_range = date.today() + timedelta(weeks=-1)
    end_range = date.today() + timedelta(weeks=1)

    agendamientoModel.Agendamiento.fecHorReg.between(start_range, end_range)
    stmt = text("SELECT Agendamiento.idAgend AS idAgend, Usuario.primNomUsr AS primNomUsr, "
                "Usuario.segNomUsr AS segNomUsr, Usuario.primApeUsr AS primApeUsr, "
                "HorarioMateriaGrupo.Horario AS Horario, HorarioMateriaGrupo.Salon AS Salon, "
                "HorarioMateriaGrupo.Edificio AS Edificio, HorarioMateriaGrupo.Profesor AS Profesor "
                "FROM Agendamiento JOIN Usuario ON Usuario.idUsuario = Agendamiento.idUsuario "
                "JOIN HorarioMateriaGrupo ON Agendamiento.idHorMatGrp = HorarioMateriaGrupo.idHorMatGrp "
                "JOIN MateriaGrupo ON MateriaGrupo.idMatGrp = HorarioMateriaGrupo.idMatGrp "
                "JOIN Materia ON Materia.idMat = MateriaGrupo.idMat "
                "WHERE Materia.idMat =:ID_MAT "
                "AND Agendamiento.fecHorReg >=:start_range "
                "AND Agendamiento.fecHorReg <=:end_range "
                "AND Agendamiento.Asistira = 1 "). \
        bindparams(ID_MAT=ID_MAT, start_range=start_range, end_range=end_range). \
        columns(column('idAgend', Integer), column('primNomUsr', Unicode), column('segNomUsr', Unicode),
                column('primApeUsr', Unicode), column('Horario', Unicode), column('Salon', Unicode),
                column('Edificio', Unicode), column('Profesor', Unicode))

    result = db.execute(stmt)

    reservasSemanaMateria = [dict(row) for row in result]

    if not reservasSemanaMateria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No hay reservas en esta semana para la materia")
    return reservasSemanaMateria


def crear_reserva(request: agendamientoModel.Agendamiento, db: Session):

    start_range = date.today() + timedelta(weeks=-1)
    end_range = date.today() + timedelta(weeks=1)
    reservas_Semana_Curso = db.query(agendamientoModel.Agendamiento).filter(
            and_((agendamientoModel.Agendamiento.idHorMatGrp == request.idHorMatGrp),
                 (agendamientoModel.Agendamiento.idUsuario == request.idUsuario),
                 (agendamientoModel.Agendamiento.fecHorReg.between(start_range, end_range)))
    ).all()

    if len(reservas_Semana_Curso) > 0 and bool(request.idAgend):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Ya ha reservado previamente para esa clase en ese dia")

    nuevo_reserva = agendamientoModel.Agendamiento(idHorMatGrp=request.idHorMatGrp,
                                                   idUsuario=request.idUsuario,
                                                   Asistira=request.Asistira,
                                                   fecHorReg=date.today()
                                                   )
    db.add(nuevo_reserva)
    db.commit()
    db.refresh(nuevo_reserva)
    return nuevo_reserva


def modificar_reserva(request: agendamientoModel.Agendamiento, db: Session):
    start_range = date.today() + timedelta(weeks=-1)
    end_range = date.today() + timedelta(weeks=1)
    reservas_Semana_Curso = db.query(agendamientoModel.Agendamiento).filter(
            and_((agendamientoModel.Agendamiento.idAgend == request.idAgend),
                 (agendamientoModel.Agendamiento.idHorMatGrp == request.idHorMatGrp),
                 (agendamientoModel.Agendamiento.idUsuario == request.idUsuario),
                 (agendamientoModel.Agendamiento.fecHorReg.between(start_range, end_range)),
                 (agendamientoModel.Agendamiento.Asistira == request.Asistira))
    ).all()

    if len(reservas_Semana_Curso) > 0:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Ya ha reservado previamente para esa clase en ese dia")

    reserva_actualizado = db.query(agendamientoModel.Agendamiento).filter(
            agendamientoModel.Agendamiento.idAgend == request.idAgend).first()
    if not reserva_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"La reserva con id {request.idAgend} no esta disponible")

    reserva_actualizado.idAgend = request.idAgend
    reserva_actualizado.idHorMatGrp = request.idHorMatGrp
    reserva_actualizado.idUsuario = request.idUsuario
    reserva_actualizado.Asistira = request.Asistira

    db.commit()
    db.refresh(reserva_actualizado)
    return reserva_actualizado
