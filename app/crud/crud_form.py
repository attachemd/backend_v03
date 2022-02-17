from app.crud.crud_base import CRUDBase


class CRUDForm(CRUDBase[Form, FormCreate, FormUpdate]):
    pass


form = CRUDForm(Form)
