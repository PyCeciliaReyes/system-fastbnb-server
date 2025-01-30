from app.adapters.repositories.user_repository import UserRepository

class DeleteUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, user_id: int) -> None:
        await self.repository.delete(user_id)