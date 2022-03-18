from typing import Optional

from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models.client import Client
from app.schemas import ClientCreate, ClientUpdate


class CRUDClient(CRUDBase[Client, ClientCreate, ClientUpdate]):
    pass
    # def get_by_name(
    #     self, db: Session, *, name: str
    # ) -> Optional[Client]:
    #     return (
    #         db.query(self.model).filter(Client.name == name).first()
    #     )
    def get_by_email(
        self, db: Session, *, email: str
    ) -> Optional[Client]:
        return (
            db.query(Client)
            .filter(Client.email == email)
            .first()
        )


client = CRUDClient(Client)
