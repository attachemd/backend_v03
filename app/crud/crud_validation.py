from app.crud.crud_base import CRUDBase
from app.models.validation import Validation
from app.schemas import ValidationCreate, ValidationUpdate


class CRUDValidation(CRUDBase[Validation, ValidationCreate, ValidationUpdate]):
    pass


validation = CRUDValidation(Validation)