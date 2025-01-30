# app/infrastructure/main.py
from fastapi import FastAPI
from app.infrastructure.database import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()  # Conectar a la BD

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()  # Desconectar de la BD

@app.get("/")
async def home():
    return {"message": "API conectada a la base de datos correctamente!"}
