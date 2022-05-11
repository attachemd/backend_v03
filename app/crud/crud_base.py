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
from fastapi import HTTPException

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db import session

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
        # print('obj_in_data')
        # print(obj_in_data)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def bulk_create(
        self,
        db: Session,
        *,
        objs_in: List[CreateSchemaType]
    ) -> ModelType:
        db_objs = list()
        for obj_in in objs_in:
            # db_obj = FormElementOption(
            #     value=obj_in.value,
            #     form_element_field_id=obj_in.form_element_field_id,
            # )
            obj_in_data = jsonable_encoder(obj_in)
            # print('obj_in_data')
            # print(obj_in_data)
            # db_obj = self.model(**obj_in_data)
            # db_objs.append(db_obj)
            db_objs.append(obj_in_data)
            
        # db.bulk_save_objects(db_objs)
        
        # db.add_all(db_objs)
        
        # db.commit()
        
        session.engine.execute(
            self.model.__table__.insert(),
            db_objs,
        )
        
        # db.bulk_insert_mappings(self.model, db_objs)
        
        # try:
        #     db.bulk_save_objects(db_objs)
        # except Exception as e:
        #     print(e)
        #     raise HTTPException(status_code=404, detail="Row not found")
        # finally:
        #     db.commit()
        return "Ok"
    
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
    
    def delete(self, db: Session, *, obj_id: int):
        row = db.query(self.model).filter(self.model.id == obj_id).first()
        if not row:
            raise HTTPException(status_code=404, detail="Row not found")
        db.delete(row)
        db.commit()
        return "Ok"