from typing import Optional
from app.crud.crud_base import CRUDBase
from app.models.form_element_template import FormElementTemplate
from app.schemas import FormElementTemplateCreate, FormElementTemplateUpdate
from sqlalchemy.orm import Session


class CRUDFormElementTemplate(CRUDBase[FormElementTemplate, FormElementTemplateCreate, FormElementTemplateUpdate]):
    def get_by_form_element_type_id(
        self, db: Session, *, form_element_type_id: str
    ) -> Optional[FormElementTemplate]:
        return (
            db.query(FormElementTemplate)
            .filter(FormElementTemplate.form_element_type_id == form_element_type_id)
            .first()
        )


form_element_template = CRUDFormElementTemplate(FormElementTemplate)
