""" Creado por Daniel Diaz
    Ultima modificación: 17 marzo 2025
    Archivo para conectarse a una base de datos de acuerdo a la url ubicada en config
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException
from passlib.context import CryptContext

from src.models import User
from src.schemas.user_schemas import UserCreate

# Configuración para encriptar contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_users(db: Session):
    """ Obtener todos los usuarios """
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    """ Obtener un usuario por ID """
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    """ Crear un nuevo usuario con validaciones """
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    hashed_password = pwd_context.hash(user.password)  # Encriptar la contraseña
    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db: Session, user_id: int, user: UserCreate):
    """ Actualizar los datos de un usuario """
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    existing_user.name = user.name
    existing_user.email = user.email
    existing_user.password = pwd_context.hash(user.password)

    db.commit()
    return existing_user

def delete_user(db: Session, user_id: int):
    """ Eliminar un usuario """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(user)
    db.commit()