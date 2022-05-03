from app.crud.crud_base import CRUDBase
from app.db import session
from app.models.validator import Validator
from app.schemas import ValidatorCreate, ValidatorUpdate
from sqlalchemy.orm import Session


class CRUDValidator(
    CRUDBase[Validator, ValidatorCreate, ValidatorUpdate]
):
    def coco(self, db: Session):
        # Validator.__table__.insert().execute([{'name': 'blue'},
        #                             {'name': 'red'},
        #                             {'name': 'green'}])
        session.engine.execute(
            Validator.__table__.insert(),
            [{"name": "blue"}, {"name": "red"}, {"name": "green"}],
        )


validator = CRUDValidator(Validator)
