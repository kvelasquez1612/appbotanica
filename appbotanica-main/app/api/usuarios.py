from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import obtener_sesion
from models import Usuario
from schemas import UsuarioRegistro, UsuarioLogin, UsuarioRespuesta, UsuarioActualizar, Token
from auth import encriptar_password, verificar_password, crear_token_acceso, obtener_usuario_actual

router = APIRouter(prefix="/usuarios", tags=["Usuarios y Autenticación"])

@router.post("/registro", response_model=UsuarioRespuesta, status_code=status.HTTP_201_CREATED)
def registrar_usuario(datos: UsuarioRegistro, db: Session = Depends(obtener_sesion)):
    usuario_existente = db.query(Usuario).filter(Usuario.correo == datos.correo).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El correo ya se encuentra registrado")
    
    nuevo_usuario = Usuario(
        nombre=datos.nombre,
        correo=datos.correo,
        password_hash=encriptar_password(datos.password),
        rol=datos.rol
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.post("/login", response_model=Token)
def iniciar_sesion(datos: UsuarioLogin, db: Session = Depends(obtener_sesion)):
    usuario = db.query(Usuario).filter(Usuario.correo == datos.correo).first()
    if not usuario or not verificar_password(datos.password, usuario.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = crear_token_acceso(data={"sub": usuario.correo})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/perfil", response_model=UsuarioRespuesta)
def consultar_perfil(usuario_actual: Usuario = Depends(obtener_usuario_actual)):
    return usuario_actual

@router.put("/perfil", response_model=UsuarioRespuesta)
def actualizar_perfil(
    datos: UsuarioActualizar, 
    usuario_actual: Usuario = Depends(obtener_usuario_actual), 
    db: Session = Depends(obtener_sesion)
):
    if datos.nombre is not None:
        usuario_actual.nombre = datos.nombre
    if datos.correo is not None:
        correo_existente = db.query(Usuario).filter(Usuario.correo == datos.correo).first()
        if correo_existente and correo_existente.id != usuario_actual.id:
            raise HTTPException(status_code=400, detail="El correo ya está en uso por otro usuario")
        usuario_actual.correo = datos.correo
    if datos.password is not None:
        usuario_actual.password_hash = encriptar_password(datos.password)
        
    db.commit()
    db.refresh(usuario_actual)
    return usuario_actual