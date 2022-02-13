from typing import List, Any
from app import crud, models, schemas, exceptions
from app.constants.role import Role
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session

from app.api import deps

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.get("/", response_model=List[schemas.Account])
def get_accounts(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Retrieve all accounts.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    accounts = crud.account.get_multi(db)
    return accounts
