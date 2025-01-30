from sqlalchemy import text
from app.entities.user import User
from app.infrastructure.database import database
from app.infrastructure.models import users_table
from typing import List, Optional
import bcrypt

class UserRepository:
    async def get_all(self) -> List[User]:
        query = users_table.select()
        rows = await database.fetch_all(query)
        return [User(**dict(row)) for row in rows]

    async def get_by_id(self, user_id: int) -> Optional[User]:
        query = users_table.select().where(users_table.c.id == user_id)
        row = await database.fetch_one(query)
        return User(**dict(row)) if row else None

    # async def save(self, user: User) -> User:
    #     hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
    #     query = users_table.insert().values(
    #         name=user.name,
    #         email=user.email,
    #         password=hashed_password,
    #         phone_number=user.phone_number,
    #         description=user.description,
    #         profile_image=user.profile_image
    #     ).returning(users_table.c.id)
        
    #     user_id = await database.execute(query)
    #     user.id = user_id
    #     return user
    async def save(self, user: User) -> User:
        hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
        
        # Inserción sin RETURNING
        query = users_table.insert().values(
            name=user.name,
            email=user.email,
            password=hashed_password,
            phone_number=user.phone_number,
            description=user.description,
            profile_image=user.profile_image
        )

        # Ejecutar inserción
        await database.execute(query)

        # Obtener el último ID insertado con LAST_INSERT_ID()
        user_id = await database.fetch_val(text("SELECT LAST_INSERT_ID()"))

        # Asignar ID al usuario y retornarlo
        user.id = user_id
        return user

    async def update(self, user_id: int, user_data: dict) -> Optional[User]:
        query = users_table.update().where(users_table.c.id == user_id).values(**user_data)
        await database.execute(query)
        return await self.get_by_id(user_id)

    async def delete(self, user_id: int) -> None:
        query = users_table.delete().where(users_table.c.id == user_id)
        await database.execute(query)