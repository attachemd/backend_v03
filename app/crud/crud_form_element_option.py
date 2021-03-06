from typing import List

from sqlalchemy import delete
from app.crud.crud_base import CRUDBase
from app.models.form_element_option import FormElementOption
from app.schemas import (
    FormElementOptionCreate,
    FormElementOptionUpdate,
)
from sqlalchemy.orm import Session
from app.db import session


class CRUDFormElementOption(
    CRUDBase[
        FormElementOption,
        FormElementOptionCreate,
        FormElementOptionUpdate,
    ]
):
    # def bulk_create(
    #     self,
    #     db: Session,
    #     *,
    #     objs_in: List[FormElementOptionCreate]
    # ) -> FormElementOption:
    #     db_objs = list()
    #     for obj_in in objs_in:
    #         db_obj = FormElementOption(
    #             value=obj_in.value,
    #             form_element_field_id=obj_in.form_element_field_id,
    #         )
    #         db_objs.append(db_obj)
    #     db.bulk_save_objects(db_objs)
    #     db.commit()
    #     return "Ok"

    def get_by_name_and_form_element_field_id(
        self,
        db: Session,
        *,
        form_element_field_id: str,
        value: str
    ) -> FormElementOption:
        return (
            db.query(self.model)
            .filter(
                FormElementOption.form_element_field_id
                == form_element_field_id
                and FormElementOption.value == value.lower()
            )
            .first()
        )

    def delete_by_form_element_field_id(
        self, db: Session, *, form_element_field_id: str
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
            self.model.form_element_field_id == form_element_field_id
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


form_element_option = CRUDFormElementOption(
    FormElementOption
)
