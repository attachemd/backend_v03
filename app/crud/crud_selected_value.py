from typing import List
from app.crud.crud_base import CRUDBase
from app.models.selected_value import SelectedValue
from app.schemas import SelectedValueCreate, SelectedValueUpdate
from sqlalchemy.orm import Session


class CRUDSelectedValue(
    CRUDBase[SelectedValue, SelectedValueCreate, SelectedValueUpdate]
):
    def get_by_form_element_field_id(
        self, db: Session, *, form_element_field_id: str
    ) -> SelectedValue:
        return (
            db.query(SelectedValue)
            .filter(SelectedValue.form_element_field_id == form_element_field_id)
            .first()
        )


selected_value = CRUDSelectedValue(SelectedValue)
