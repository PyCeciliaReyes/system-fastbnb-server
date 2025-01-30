# app/infrastructure/models.py
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from app.infrastructure.database import metadata

# Tabla de Usuarios
users_table = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("email", String(255), unique=True, nullable=False),
    Column("email_verified_at", DateTime, nullable=True),
    Column("password", String(255), nullable=False),
    Column("remember_token", String(100), nullable=True),
    Column("created_at", DateTime, default=func.now()),
    Column("updated_at", DateTime, default=func.now(), onupdate=func.now()),
    Column("phone_number", String(20), nullable=False),
    Column("description", String(500), nullable=True),
    Column("profile_image", String(255), nullable=True),
)

# Tabla de Rooms
rooms_table = Table(
    "rooms", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("home_type", String(255), nullable=False),
    Column("room_type", String(255), nullable=False),
    Column("total_occupancy", Integer, nullable=False),
    Column("total_bedrooms", Integer, nullable=False),
    Column("total_bathrooms", Integer, nullable=False),
    Column("summary", String(500), nullable=False),
    Column("address", String(255), nullable=False),
    Column("has_tv", Boolean, default=False),
    Column("has_kitchen", Boolean, default=False),
    Column("has_air_con", Boolean, default=False),
    Column("has_heating", Boolean, default=False),
    Column("has_internet", Boolean, default=False),
    Column("price", Integer, nullable=False),
    Column("published_at", DateTime, nullable=True),
    Column("owner_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("created_at", DateTime, default=func.now()),
    Column("updated_at", DateTime, default=func.now(), onupdate=func.now()),
    Column("latitude", Float, nullable=False),
    Column("longitude", Float, nullable=False),
)

# Tabla de Reservaciones
reservations_table = Table(
    "reservations", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
    Column("room_id", Integer, ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False),
    Column("start_date", DateTime, nullable=False),
    Column("end_date", DateTime, nullable=False),
    Column("price", Integer, nullable=False),
    Column("total", Integer, nullable=False),
    Column("created_at", DateTime, default=func.now()),
    Column("updated_at", DateTime, default=func.now(), onupdate=func.now()),
)

# Tabla de Reseñas
reviews_table = Table(
    "reviews", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("reservation_id", Integer, ForeignKey("reservations.id", ondelete="CASCADE"), nullable=False),
    Column("rating", Integer, nullable=False),
    Column("comment", String(1000), nullable=True),
)

# Tabla de Medios
media_table = Table(
    "media", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("model_id", Integer, nullable=False),
    Column("model_type", String(255), nullable=False),
    Column("file_name", String(255), nullable=False),
    Column("mime_type", String(100), nullable=True),
)