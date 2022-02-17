from app.crud.crud_base import CRUDBase
from app.models.form_element import FormElement
from app.schemas import FormElementCreate, FormElementUpdate


class CRUDFormElement(CRUDBase[FormElement, FormElementCreate, FormElementUpdate]):
    pass


form_element = CRUDFormElement(FormElement)
