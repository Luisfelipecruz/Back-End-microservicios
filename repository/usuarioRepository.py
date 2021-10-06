from fastapi import HTTPException, status
from sqlalchemy import Integer, Unicode, DateTime, String
from schemas import usuarioSchema
from models import usuarioModel, horarioMateriaModel
from sqlalchemy.sql import column, text
from sqlalchemy.orm import Session


def listar_usuarios(db: Session):
    usuarios = db.query(usuarioModel.Usuario).all()
    return usuarios


def bucar_usuario(_id: int, db: Session):
    usuario = db.query(usuarioModel.Usuario).filter(usuarioModel.Usuario.CodEst == _id).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El usuario con id {_id} no esta disponible")
    return usuario


def bucar_materiaEstudiante_codigo(codigo: int, db: Session):
    stmt = text("SELECT MateriaEstudiante.idMatEst AS idMatEst, Materia.nombre AS nombre, MateriaGrupo.Grupo AS Grupo "
                "FROM Usuario JOIN MateriaEstudiante ON Usuario.idUsuario = MateriaEstudiante.idUsuario "
                "JOIN MateriaGrupo ON MateriaGrupo.idMatGrp = MateriaEstudiante.idMatGrp "
                "JOIN Materia ON Materia.idMat = MateriaGrupo.idMat "
                "WHERE (Usuario.CodEst =:cod)"). \
        bindparams(cod=codigo). \
        columns(column('idMatEst', Integer), column('nombre', Unicode), column('Grupo', Unicode))
    result = db.execute(stmt)
    usuarioMaterias = [dict(row) for row in result]

    if not usuarioMaterias:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No hay registro con el codigo de estudiante {codigo} ")
    return usuarioMaterias


def bucar_materiaEstudianteHorario_codigo(request: usuarioSchema.codigoUsuario, db: Session):
    codigo = request.CodEst
    stmt = text("SELECT MateriaEstudiante.idMatEst AS idMatEst, Materia.nombre AS nombre,"
                " MateriaGrupo.Grupo AS Grupo, MateriaGrupo.idMatGrp AS idMatGrp "
                "FROM Usuario JOIN MateriaEstudiante ON Usuario.idUsuario = MateriaEstudiante.idUsuario "
                "JOIN MateriaGrupo ON MateriaGrupo.idMatGrp = MateriaEstudiante.idMatGrp "
                "JOIN Materia ON Materia.idMat = MateriaGrupo.idMat "
                "WHERE (Usuario.CodEst =:cod)"). \
        bindparams(cod=codigo). \
        columns(column('idMatEst', Integer), column('nombre', Unicode),
                column('Grupo', Unicode), column('idMatGrp', Integer))

    result = db.execute(stmt)
    usuarioMaterias = [dict(row) for row in result]

    for registro in usuarioMaterias:
        horario_materias = db.query(horarioMateriaModel.HorarioMateriaGrupo).filter(
                horarioMateriaModel.HorarioMateriaGrupo.idMatGrp == registro["idMatGrp"])
        horario_materias_List = [row for row in horario_materias]
        registro["horario"] = horario_materias_List

    if not usuarioMaterias:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No hay registro con el codigo de estudiante {codigo} ")
    return usuarioMaterias


def crear_usuario(request: usuarioSchema.Usuario, db: Session):
    nuevo_usuarios = usuarioModel.Usuario(idRol=request.idRol,
                                          CodEst=request.CodEst,
                                          email=request.email,
                                          primNomUsr=request.primNomUsr,
                                          segNomUsr=request.segNomUsr,
                                          primApeUsr=request.primApeUsr,
                                          SegmApeUsr=request.SegmApeUsr,
                                          generoUsr=request.generoUsr
                                          )
    db.add(nuevo_usuarios)
    db.commit()
    db.refresh(nuevo_usuarios)
    return nuevo_usuarios


def loguearUsuario(request: usuarioSchema.singInCaptura, db: Session):
    validacion = db.query(usuarioModel.Usuario).filter(usuarioModel.Usuario.CodEst == request.usuario).first()

    singInRespuesta = usuarioSchema.singInRespuesta(CodEst=request.usuario)

    if (request.usuario == request.pasword) and bool(validacion):
        singInRespuesta = usuarioSchema.singInRespuesta(idUsuario=validacion.idUsuario,
                                                        idRol=validacion.idRol,
                                                        CodEst=validacion.CodEst,
                                                        primNomUsr=validacion.primNomUsr,
                                                        segNomUsr=validacion.segNomUsr,
                                                        primApeUsr=validacion.primApeUsr,
                                                        SegmApeUsr=validacion.SegmApeUsr,
                                                        generoUsr=validacion.generoUsr,
                                                        respuesta=True
                                                        )
    else:
        singInRespuesta.respuesta = False
    return singInRespuesta


def modificar_usuario(_id: int, request: usuarioSchema.Usuario, db: Session):
    usuario_actualizado = db.query(usuarioModel.Usuario).filter(usuarioModel.Usuario.idUsuario == _id).first()
    if not usuario_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El usuario con id {_id} no esta disponible")

    usuario_actualizado.idRol = request.idRol
    usuario_actualizado.email = request.email
    usuario_actualizado.primNomUsr = request.primNomUsr
    usuario_actualizado.segNomUsr = request.segNomUsr
    usuario_actualizado.primApeUsr = request.primApeUsr
    usuario_actualizado.SegmApeUsr = request.SegmApeUsr
    usuario_actualizado.generoUsr = request.generoUsr

    db.commit()
    db.refresh(usuario_actualizado)
    return usuario_actualizado


def eliminar_usuario(_id: int, db: Session):
    usuario = db.query(usuarioModel.Usuario).filter(usuarioModel.Usuario.idUsuario == _id).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"El usuario con id {_id} no esta disponible")
    else:
        usuario.delete(synchronize_session=False)
    db.commit()
    return 'eliminado'
