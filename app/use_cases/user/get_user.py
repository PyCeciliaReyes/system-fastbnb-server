from app.adapters.repositories.user_repository import UserRepository
from app.entities.user import User
from typing import Optional

class GetUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, user_id: int) -> Optional[User]:
        return await self.repository.get_by_id(user_id)