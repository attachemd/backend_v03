from app.crud.crud_base import CRUDBase
from app.models.form_element_field import FormElementField
from app.schemas import FormElementFieldCreate, FormElementFieldUpdate


class CRUDFormElementField(
    CRUDBase[
        FormElementField, FormElementFieldCreate, FormElementFieldUpdate
    ]
):
    pass


form_element_field = CRUDFormElementField(FormElementField)
