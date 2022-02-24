from app.crud.crud_base import CRUDBase
from app.models.selected_list_value import (
    SelectedListValue,
)
from app.schemas import (
    SelectedListValueCreate,
    SelectedListValueUpdate,
)


class CRUDSelectedListValue(
    CRUDBase[
        SelectedListValue,
        SelectedListValueCreate,
        SelectedListValueUpdate,
    ]
):
    pass


selected_list_value = CRUDSelectedListValue(
    SelectedListValue
)
