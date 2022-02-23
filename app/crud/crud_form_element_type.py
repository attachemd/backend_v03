from typing import Optional
from app.crud.crud_base import CRUDBase
from app.models.form_element_type import FormElementType
from app.schemas import FormElementTypeCreate, FormElementTypeUpdate
from sqlalchemy.orm import Session


class CRUDFormElementType(
    CRUDBase[
        FormElementType, FormElementTypeCreate, FormElementTypeUpdate
    ]
):
    pass
    # def get_by_name(
    #     self, db: Session, *, name: str
    # ) -> Optional[FormElementType]:
    #     return (
    #         db.query(self.model).filter(FormElementType.name == name).first()
    #     )


form_element_type = CRUDFormElementType(FormElementType)
