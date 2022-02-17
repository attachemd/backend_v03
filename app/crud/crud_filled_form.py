from app.crud.crud_base import CRUDBase
from app.models.filled_form import FilledForm
from app.schemas import FilledFormCreate, FilledFormUpdate


class CRUDFilledForm(
    CRUDBase[FilledForm, FilledFormCreate, FilledFormUpdate]
):
    pass


filled_form = CRUDFilledForm(FilledForm)
