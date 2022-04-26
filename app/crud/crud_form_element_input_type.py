from app.crud.crud_base import CRUDBase
from app.models.form_element_input_type import FormElementInputType
from app.schemas import FormElementInputTypeCreate, FormElementInputTypeUpdate


class CRUDFormElementInputType(CRUDBase[FormElementInputType, FormElementInputTypeCreate, FormElementInputTypeUpdate]):
    pass


form_element_input_type = CRUDFormElementInputType(FormElementInputType)