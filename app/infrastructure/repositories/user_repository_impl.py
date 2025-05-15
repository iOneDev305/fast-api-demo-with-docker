from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.models.user import User
from app.domain.repositories.user_repository import UserRepository

class UserRepositoryImpl(UserRepository):

    def get_all(self, db: Session) -> List[User]:
        return db.query(User).all()

    def get_by_id(self, db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()
