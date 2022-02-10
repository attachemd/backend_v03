from typing import Optional, List

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.schemas import UserCreate


class CRUDUser:
    def __init__(self, model):
        """Base class that can be extend by other action classes.
           Provides basic CRUD and listing operations.

        :param model: The SQLAlchemy model
        :type model: Type[ModelType]
        """
        self.model = model

    def get(self, db: Session, id: str):
        return (
            db.query(self.model).filter(self.model.id == id).first()
        )

    def get_by_email(
            self, db: Session, *, email: str
    ) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            phone_number=obj_in.phone_number,
            # account_id=obj_in.account_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def is_active(self, user: User) -> bool:
        return user.is_active

    def get_multi(
            self, db: Session
    ) -> List[User]:
        return db.query(self.model).all()

    def authenticate(
            self, username: str, password: str, db: Session
    ) -> Optional[User]:
        user = (
            db.query(self.model)
                .filter(self.model.email == username)
                .first()
        )

        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user


# TODO injecting user
user = CRUDUser(User)
