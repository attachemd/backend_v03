from typing import (
    Generic,
    TypeVar,
    Type,
    Optional,
    List,
    Union,
    Dict,
    Any,
)

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base import Base

# Define custom types for SQLAlchemy model, and Pydantic schemas
ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(
    Generic[ModelType, CreateSchemaType, UpdateSchemaType]
):
    def __init__(self, model: Type[ModelType]):
        """Base class that can be extend by other action classes.
           Provides basic CRUD and listing operations.

        :param model: The SQLAlchemy model
        :type model: Type[ModelType]
        """
        self.model = model

    def get(self, db: Session, obj_id: str) -> Optional[ModelType]:
        return (
            db.query(self.model)
            .filter(self.model.id == obj_id)
            .first()
        )

    def get_by_name(
        self, db: Session, *, name: str
    ) -> Optional[ModelType]:
        return (
            db.query(self.model)
            .filter(self.model.name == name)
            .first()
        )

    def get_multi(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()

    def create(
        self, db: Session, *, obj_in: CreateSchemaType
    ) -> ModelType:
        # TODO jsonable_encoder
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
