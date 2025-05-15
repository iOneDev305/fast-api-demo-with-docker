from typing import List, Optional
from app.domain.models.user import User
from app.domain.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self, db: Session) -> List[User]:
        return self.user_repository.get_all(db)

    def get_user_by_id(self, db: Session, user_id: int) -> Optional[User]:
        return self.user_repository.get_by_id(db, user_id)
