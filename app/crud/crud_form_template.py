from app.crud.crud_base import CRUDBase
from app.models.form_template import FormTemplate
from app.schemas import FormTemplateCreate, FormTemplateUpdate


class CRUDFormTemplate(
    CRUDBase[
        FormTemplate, FormTemplateCreate, FormTemplateUpdate
    ]
):
    pass


form_template = CRUDFormTemplate(FormTemplate)
