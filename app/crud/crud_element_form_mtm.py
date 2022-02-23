from app.crud.crud_base import CRUDBase
from app.models.element_form_mtm import ElementFormMTM
from app.schemas import ElementFormMTMCreate, ElementFormMTMUpdate


class CRUDElementFormMTM(
    CRUDBase[
        ElementFormMTM, ElementFormMTMCreate, ElementFormMTMUpdate
    ]
):
    pass


element_form_mtm = CRUDElementFormMTM(ElementFormMTM)
