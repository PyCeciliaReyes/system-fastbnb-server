# app/infrastructure/database.py
from databases import Database
from sqlalchemy import create_engine, MetaData
from app.config import settings

# Configurar SQLAlchemy con la URL de la base de datos
database = Database(settings.DATABASE_URL)
engine = create_engine(settings.DATABASE_URL)

# Metadata para manejar la base de datos ya existente
metadata = MetaData()