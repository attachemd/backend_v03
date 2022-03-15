from typing import Optional

from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models.account import Account
from app.schemas import AccountCreate, AccountUpdate


class CRUDAccount(CRUDBase[Account, AccountCreate, AccountUpdate]):
    pass
    # def get_by_name(
    #     self, db: Session, *, name: str
    # ) -> Optional[Account]:
    #     return (
    #         db.query(self.model).filter(Account.name == name).first()
    #     )
    def get_by_email(
        self, db: Session, *, email: str
    ) -> Optional[Account]:
        return (
            db.query(Account)
            .filter(Account.email == email)
            .first()
        )


account = CRUDAccount(Account)
