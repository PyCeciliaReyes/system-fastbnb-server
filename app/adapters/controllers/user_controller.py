from fastapi import APIRouter, Depends, HTTPException
from app.adapters.repositories.user_repository import UserRepository
from app.use_cases.user.create_user import CreateUserUseCase
from app.use_cases.user.get_user import GetUserUseCase
from app.use_cases.user.update_user import UpdateUserUseCase
from app.use_cases.user.delete_user import DeleteUserUseCase
from app.entities.user import User
from typing import List

router = APIRouter()

@router.get("/users", response_model=List[User])
async def get_all_users(repository: UserRepository = Depends()):
    return await repository.get_all()

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, repository: UserRepository = Depends()):
    use_case = GetUserUseCase(repository)
    user = await use_case.execute(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.post("/users", response_model=User)
async def create_user(user_data: User, repository: UserRepository = Depends()):
    use_case = CreateUserUseCase(repository)
    return await use_case.execute(user_data.dict())

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user_data: dict, repository: UserRepository = Depends()):
    use_case = UpdateUserUseCase(repository)
    user = await use_case.execute(user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, repository: UserRepository = Depends()):
    use_case = DeleteUserUseCase(repository)
    await use_case.execute(user_id)
    return {"message": "Usuario eliminado correctamente"}