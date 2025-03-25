from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.apiroutes.endpoints import router
from src.apiroutes.auth import auth_router
from src.core.config import settings
from src.db.database import engine, Base, get_db, test_connection

# Crear tablas en la BD si no existen
Base.metadata.create_all(bind=engine)

test_connection()

app = FastAPI(
    title="Micro CRUD Python",
    description="API REST con FastAPI, SQLAlchemy y Pydantic",
    version="1.0.0",
    debug=False  # Se toma desde el .env
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods = ['*'],
    allow_headers = ['*']
)

app.include_router(router, prefix="/api")

app.include_router(auth_router, prefix="/auth")

@app.get("/")
def root():
    return {"message": "Bienvenido a la API 🚀"}

if __name__ == "__main__":
    # Código que solo se ejecuta si el script se ejecuta directamente
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
