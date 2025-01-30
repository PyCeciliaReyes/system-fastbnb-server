from app.entities.user import User
from app.adapters.repositories.user_repository import UserRepository

class CreateUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, user_data: dict) -> User:
        user = User(**user_data)
        return await self.repository.save(user)