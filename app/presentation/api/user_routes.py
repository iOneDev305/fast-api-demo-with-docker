from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.domain.models.user import User
from app.application.services.user_service import UserService

def create_user_routes(user_service: UserService) -> APIRouter:
    router = APIRouter()

    @router.get("/users", response_model=List[User])
    def get_users():
        return user_service.get_all_users()

    @router.get("/users/{user_id}", response_model=User)
    def get_user(user_id: int):
        user = user_service.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    return router
