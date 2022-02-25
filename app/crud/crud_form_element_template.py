from app.crud.crud_base import CRUDBase
from app.models.form_element_template import FormElementTemplate
from app.schemas import FormElementTemplateCreate, FormElementTemplateUpdate


class CRUDFormElementTemplate(
    CRUDBase[
        FormElementTemplate, FormElementTemplateCreate, FormElementTemplateUpdate
    ]
):
    pass


form_element_template = CRUDFormElementTemplate(FormElementTemplate)
