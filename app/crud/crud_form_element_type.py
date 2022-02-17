from app.crud.crud_base import CRUDBase
from app.models.form_element_type import FormElementType
from app.schemas import FormElementTypeCreate, FormElementTypeUpdate


class CRUDFormElementType(
    CRUDBase[
        FormElementType, FormElementTypeCreate, FormElementTypeUpdate
    ]
):
    pass


form_element_type = CRUDFormElementType(FormElementType)
