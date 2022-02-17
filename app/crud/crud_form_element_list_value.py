from app.crud.crud_base import CRUDBase
from app.models.form_element_list_value import FormElementListValue
from app.schemas import (
    FormElementListValueCreate,
    FormElementListValueUpdate,
)


class CRUDFormElementListValue(
    CRUDBase[
        FormElementListValue,
        FormElementListValueCreate,
        FormElementListValueUpdate,
    ]
):
    pass


form_element_list_value = CRUDFormElementListValue(FormElementListValue)
