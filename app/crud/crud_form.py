from app.crud.crud_base import CRUDBase
from app.models.form import Form
from app.schemas import FormCreate, FormUpdate


class CRUDForm(CRUDBase[Form, FormCreate, FormUpdate]):
    pass


form = CRUDForm(Form)
