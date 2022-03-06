from typing import List, Optional
from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models.user_role import UserRole
from app.schemas import UserRoleCreate, UserRoleUpdate


class CRUDUserRole(CRUDBase[UserRole, UserRoleCreate, UserRoleUpdate]):
    def get_by_user_id(
        self, db: Session, *, user_id: str
    ) -> List[UserRole]:
        return db.query(UserRole).filter(UserRole.user_id == user_id).all()


user_role = CRUDUserRole(UserRole)
