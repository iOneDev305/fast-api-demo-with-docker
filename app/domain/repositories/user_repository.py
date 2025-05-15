from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.models.user import User
from sqlalchemy.orm import Session

class UserRepository(ABC):
    @abstractmethod
    def get_all(self, db: Session) -> List[User]:
        pass

    @abstractmethod
    def get_by_id(self, db: Session, user_id: int) -> Optional[User]:
        pass
