from app.crud.crud_base import CRUDBase
from app.models.validator import Validator
from app.schemas import ValidatorCreate, ValidatorUpdate


class CRUDValidator(CRUDBase[Validator, ValidatorCreate, ValidatorUpdate]):
    pass


validator = CRUDValidator(Validator)