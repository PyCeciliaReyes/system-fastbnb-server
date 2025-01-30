from app.adapters.repositories.user_repository import UserRepository
from app.entities.user import User
from typing import Optional

class UpdateUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, user_id: int, user_data: dict) -> Optional[User]:
        return await self.repository.update(user_id, user_data)