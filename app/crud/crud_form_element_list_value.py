from typing import List

from sqlalchemy import delete
from app.crud.crud_base import CRUDBase
from app.models.form_element_list_value import FormElementListValue
from app.schemas import (
    FormElementListValueCreate,
    FormElementListValueUpdate,
)
from sqlalchemy.orm import Session
from app.db import session


class CRUDFormElementListValue(
    CRUDBase[
        FormElementListValue,
        FormElementListValueCreate,
        FormElementListValueUpdate,
    ]
):
    def get_by_name_and_form_element_id(
        self,
        db: Session,
        *,
        form_element_template_id: str,
        value: str
    ) -> FormElementListValue:
        return (
            db.query(self.model)
            .filter(
                FormElementListValue.form_element_template_id
                == form_element_template_id
                and FormElementListValue.value == value.lower()
            )
            .first()
        )

    def delete_by_form_element_template_id(
        self, db: Session, *, form_element_template_id: str
    ):
        # rows = db.query(self.model).filter(
        #     self.model.form_element_template_id
        #     == form_element_template_id
        # )

        # db.query(self.model).filter(
        #     self.model.form_element_template_id
        #     == form_element_template_id
        # ).delete()

        # delete_q = self.model.__table__.delete().where(
        #     self.model.form_element_template_id
        #     == form_element_template_id
        # )
        # session.engine.execute(delete_q)
        # db.session.execute(delete_q)
        # db.session.commit()

        statement = delete(self.model).where(
            self.model.form_element_template_id
            == form_element_template_id
        )
        # session.exec(statement)
        session.engine.execute(statement)
        # rows = query.statement.execute().fetchall()
        # for row in rows:
        #     print("row")
        #     print(row)
        # if not row:
        #     raise HTTPException(status_code=404, detail="Row not found")
        # db.delete(row)
        # db.commit()
        return "Ok"
        # return rows


form_element_list_value = CRUDFormElementListValue(
    FormElementListValue
)
