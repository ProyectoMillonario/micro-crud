""" Creado por Daniel Diaz
    Ultima modificación: 17 marzo 2025
    Archivo para conectarse a una base de datos de acuerdo a la url ubicada en config
"""

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from src.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Genera una sesión de base de datos para cada request."""
    db = SessionLocal()
    try:
        yield db  # Entrega la sesión
    finally:
        db.close()  # Cierra la sesión al finalizar

def test_connection():
    try:
        # Crear una sesión de base de datos
        db = next(get_db())
        
        # Ejecutar una consulta simple
        result = db.execute(text("SELECT 1"))
        print("Conexión exitosa:", result.fetchone())
        
        # Cerrar la sesión
        db.close()
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
