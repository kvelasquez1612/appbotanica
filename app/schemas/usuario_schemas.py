from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UsuarioRegistro(BaseModel):
    nombre: str
    correo: EmailStr
    password: str
    rol: Optional[str] = "usuario"

class UsuarioLogin(BaseModel):
    correo: EmailStr
    password: str

class UsuarioActualizar(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    password: Optional[str] = None

class UsuarioRespuesta(BaseModel):
    id: int
    nombre: str
    correo: EmailStr
    rol: str
    fecha_creacion: Optional[datetime] = None

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
