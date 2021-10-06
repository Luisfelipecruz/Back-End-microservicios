from fastapi import HTTPException, status
from sqlalchemy import Integer, Unicode, DateTime, String
from sqlalchemy.orm import Session
from schemas import usuarioSchema
from models import usuarioModel
from sqlalchemy.sql import column, text



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


def crear_usuario(request: usuarioSchema.Usuario, db: Session):
    nuevo_usuarios = usuarioModel.Usuario(idRol=request.idRol,
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


def loguearUsuario(request: usuarioSchema.singIn, db: Session):
    validacion = db.query(usuarioModel.Usuario).filter(usuarioModel.Usuario.CodEst == request.usuario).first()
    if (request.usuario == request.pasword) and bool(validacion):
        request.respuesta = True
    else:
        request.respuesta = False
    return request


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
