from app.crud.crud_base import CRUDBase
from app.models.list_value_filled_form_mtm import (
    ListValueFilledFormMTM,
)
from app.schemas import (
    ListValueFilledFormMTMCreate,
    ListValueFilledFormMTMUpdate,
)


class CRUDListValueFilledFormMTM(
    CRUDBase[
        ListValueFilledFormMTM,
        ListValueFilledFormMTMCreate,
        ListValueFilledFormMTMUpdate,
    ]
):
    pass


list_value_filled_form_mtm = CRUDListValueFilledFormMTM(
    ListValueFilledFormMTM
)
