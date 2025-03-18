# 🚀 FastAPI CRUD API

API RESTful con FastAPI y PostgreSQL, utilizando Docker para un despliegue eficiente.

---

## 📌 Características

✅ CRUD completo de usuarios  
✅ Base de datos PostgreSQL  
✅ Contenedores con Docker y Docker Compose  
✅ Manejo de variables de entorno con `.env`  
✅ Validación de datos con Pydantic  

---

## ⚡ 1️⃣ **Requisitos previos**

Antes de comenzar, asegúrate de tener instalado:

- [Python 3.11+](https://www.python.org/downloads/)
- [Docker y Docker Compose](https://www.docker.com/)
- [Git](https://git-scm.com/)

---

## 🚀 2️⃣ **Inicio rápido (Quick Start)**

### 1. Clonar el repositorio
    git clone https://github.com/ProyectoMillonario/micro-crud.git

### 2. Instalar docker y ejecutar el docker desktop
### 3. Ejecutar el siguiente comando para crear la imagen: 
        docker build -t crud-fastapi .
### 4. Ejecutar el siguiente comando para ejecutar el contenedor con la imagen
        docker run -p 8000:8000 crud-fastapi

