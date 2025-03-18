from fastapi import FastAPI
from src.apiroutes.endpoints import router
from src.core.config import settings
# from src.db.database import engine, Base

# Crear tablas en la BD si no existen
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Micro CRUD Python",
    description="API REST con FastAPI, SQLAlchemy y Pydantic",
    version="1.0.0",
    debug=False  # Se toma desde el .env
)

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Bienvenido a la API 🚀"}

if __name__ == "__main__":
    # Código que solo se ejecuta si el script se ejecuta directamente
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
