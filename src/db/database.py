""" Creado por Daniel Diaz
    Ultima modificación: 17 marzo 2025
    Archivo para conectarse a una base de datos de acuerdo a la url ubicada en config
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.core.config import settings

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Genera una sesión de base de datos para cada request."""
    db = SessionLocal()
    try:
        yield db  # Entrega la sesión
    finally:
        db.close()  # Cierra la sesión al finalizar