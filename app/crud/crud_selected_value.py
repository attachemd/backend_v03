from app.crud.crud_base import CRUDBase
from app.models.selected_value import SelectedValue
from app.schemas import SelectedValueCreate, SelectedValueUpdate


class CRUDSelectedValue(
    CRUDBase[SelectedValue, SelectedValueCreate, SelectedValueUpdate]
):
    pass


selected_value = CRUDSelectedValue(SelectedValue)
