from app.crud.crud_base import CRUDBase
from app.models.selected_fe_list_value import (
    SelectedFormElementListValue,
)
from app.schemas import (
    SelectedFormElementListValueCreate,
    SelectedFormElementListValueUpdate,
)


class CRUDSelectedFormElementListValue(
    CRUDBase[
        SelectedFormElementListValue,
        SelectedFormElementListValueCreate,
        SelectedFormElementListValueUpdate,
    ]
):
    pass


selected_form_element_list_value = CRUDSelectedFormElementListValue(
    SelectedFormElementListValue
)
