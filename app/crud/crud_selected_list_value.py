from sqlalchemy import delete
from app.crud.crud_base import CRUDBase
from app.db import session
from app.models.selected_list_value import (
    SelectedListValue,
)
from app.schemas import (
    SelectedListValueCreate,
    SelectedListValueUpdate,
)
from sqlalchemy.orm import Session


class CRUDSelectedListValue(
    CRUDBase[
        SelectedListValue,
        SelectedListValueCreate,
        SelectedListValueUpdate,
    ]
):
    def delete_by_form_element_option_id(
        self, db: Session, *, form_element_option_id: str
    ):
        statement = delete(self.model).where(
            self.model.form_element_option_id == form_element_option_id
        )
        session.engine.execute(statement)
        return "Ok"


selected_list_value = CRUDSelectedListValue(
    SelectedListValue
)
