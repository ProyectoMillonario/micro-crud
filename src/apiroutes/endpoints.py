from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.services.user_services import get_users, get_user, create_user, update_user, delete_user
from src.schemas.user_schemas import UserCreate, UserResponse

router = APIRouter()

@router.get("/hola")
def testhola():
    return {"message": "hola Daniel"}

# @router.get("/users", response_model=list[UserResponse])
# def read_users(db: Session = Depends(get_db)):
#     return get_users(db)

# @router.get("/users/{user_id}", response_model=UserResponse)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     user = get_user(db, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="Usuario no encontrado")
#     return user

# @router.post("/users", response_model=UserResponse)
# def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
#     return create_user(db, user)

# @router.put("/users/{user_id}", response_model=UserResponse)
# def update_existing_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
#     return update_user(db, user_id, user)

# @router.delete("/users/{user_id}")
# def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
#     delete_user(db, user_id)
#     return {"message": "Usuario eliminado"}
