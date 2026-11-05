from sqlalchemy import create_engine, text
from app.database import Base

# Importar todos los modelos para que SQLAlchemy los reconozca
from app.models.usuarios import UsuarioModel
from app.models.plantas import PlantaModel
from app.models.inventario import InventarioModel
from app.models.diagnostico import DiagnosticoModel
from app.models.historial import HistorialModel

# Reemplaza con tu contraseña real de Supabase
DATABASE_URL = "postgresql+psycopg2://postgres.ldmzvsubddbnjbkojtns:AC0Ntes1M1enT0@aws-0-us-east-1.pooler.supabase.com:5432/postgres"
engine = create_engine(DATABASE_URL)

print("Borrando tablas antiguas de forma limpia...")
with engine.begin() as conn:
    # CASCADE elimina las tablas y sus dependencias sin errores de orden
    conn.execute(text("DROP TABLE IF EXISTS historial, diagnostico, inventario, plantas, usuarios CASCADE;"))

print("Creando tablas nuevas con sus relaciones (Foreign Keys)...")
Base.metadata.create_all(bind=engine)

print("✔️ ¡Todas las tablas fueron creadas y conectadas con éxito!")