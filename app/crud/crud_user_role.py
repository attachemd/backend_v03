from typing import Optional, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas
from app.models.user_role import UserRole


class CRUDUserRole:
    def __init__(self, model):
        """Base class that can be extend by other action classes.
           Provides basic CRUD and listing operations.

        :param model: The SQLAlchemy model
        :type model: Type[ModelType]
        """
        self.model = model

    def create(
        self, db: Session, *, obj_in: schemas.UserRoleCreate
    ) -> UserRole:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_user_id(
        self, db: Session, *, user_id: str
    ) -> Optional[UserRole]:
        return (
            db.query(UserRole)
            .filter(UserRole.user_id == user_id)
            .first()
        )


# TODO injecting user
user_role = CRUDUserRole(UserRole)
