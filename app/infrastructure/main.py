# app/infrastructure/main.py
from fastapi import FastAPI
from app.infrastructure.database import database
from app.adapters.controllers.user_controller import router as user_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()  # Conectar a la BD

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()  # Desconectar de la BD

# @app.get("/")
# async def home():
#     return {"message": "API conectada a la base de datos correctamente!"}

app.include_router(user_router)