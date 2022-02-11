from typing import Optional, List

from sqlalchemy.orm import Session

from app import schemas
from app.models.role import Role


class CRUDRole:
    def __init__(self, model):
        """Base class that can be extend by other action classes.
           Provides basic CRUD and listing operations.

        :param model: The SQLAlchemy model
        :type model: Type[ModelType]
        """
        self.model = model

    def create(self, db: Session, *, obj_in: schemas.Role) -> Role:
        db_obj = Role(
            name=obj_in.name,
            description=obj_in.description,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(self, db: Session) -> List[Role]:
        return db.query(self.model).all()

    def get_by_name(
        self, db: Session, *, name: str
    ) -> Optional[Role]:
        return db.query(self.model).filter(Role.name == name).first()


# TODO injecting user
role = CRUDRole(Role)
