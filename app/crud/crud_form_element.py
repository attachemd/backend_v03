from typing import Optional
from app.crud.crud_base import CRUDBase
from app.models.form_element import FormElement
from app.schemas import FormElementCreate, FormElementUpdate
from sqlalchemy.orm import Session


class CRUDFormElement(CRUDBase[FormElement, FormElementCreate, FormElementUpdate]):
    def get_by_form_element_type_id(
        self, db: Session, *, form_element_type_id: str
    ) -> Optional[FormElement]:
        return (
            db.query(FormElement)
            .filter(FormElement.form_element_type_id == form_element_type_id)
            .first()
        )


form_element = CRUDFormElement(FormElement)
