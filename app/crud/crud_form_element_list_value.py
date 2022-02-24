from typing import List
from app.crud.crud_base import CRUDBase
from app.models.form_element_list_value import FormElementListValue
from app.schemas import (
    FormElementListValueCreate,
    FormElementListValueUpdate,
)
from sqlalchemy.orm import Session


class CRUDFormElementListValue(
    CRUDBase[
        FormElementListValue,
        FormElementListValueCreate,
        FormElementListValueUpdate,
    ]
):
    def get_by_name_and_form_element_id(
        self, db: Session, *, form_element_id: str, value: str
    ) -> FormElementListValue:
        return (
            db.query(self.model)
            .filter(
                FormElementListValue.form_element_id
                == form_element_id and FormElementListValue.value
                == value.lower()
            )
            .first()
        )


form_element_list_value = CRUDFormElementListValue(
    FormElementListValue
)
