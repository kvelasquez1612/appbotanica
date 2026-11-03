from pydantic import BaseModel, EmailStr, Field


# ---------- Registro ----------
class UsuarioRegistro(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=64)


# ---------- Login ----------
class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str


# ---------- Respuesta (nunca devuelve la contraseña) ----------
class UsuarioRespuesta(BaseModel):
    id: int
    nombre: str
    email: EmailStr

    class Config:
        from_attributes = True


# ---------- Token (respuesta del login) ----------
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"