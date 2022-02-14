from typing import List, Any
from app import crud, models, schemas, exceptions
from app.constants.role import Role
from fastapi import APIRouter, Depends, Security, HTTPException, Body
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
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")
    return crud.account.get_multi(db)


@router.get("/me/", response_model=schemas.Account)
def get_account_for_user(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(
        deps.get_current_active_user
    ),
) -> Any:
    """
    Retrieve account for a logged in user.
    """
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")
    return crud.account.get(db, obj_id=current_user.account_id)


@router.post("/", response_model=schemas.Account)
def create_account(
    *,
    db: Session = Depends(deps.get_db),
    account_in: schemas.AccountCreate,
    current_user: models.User = Depends(
        deps.get_current_active_user
    ),
) -> Any:
    """
    Create an user account
    """
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")
    account = crud.account.get_by_name(db, name=account_in.name)
    if account:
        raise HTTPException(
            status_code=409,
            detail="An account with this name already exists",
        )
    return crud.account.create(db, obj_in=account_in)


@router.put("/{account_id}/", response_model=schemas.Account)
def update_account(
    *,
    db: Session = Depends(deps.get_db),
    account_id: str,
    account_in: schemas.AccountUpdate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[
            Role.ADMIN["name"],
            Role.SUPER_ADMIN["name"],
            Role.ACCOUNT_ADMIN["name"],
        ],
    ),
) -> Any:
    """
    Update an account.
    """

    # If user is an account admin,
    # check ensure they update their own account.
    # TODO update_account
    if (
        current_user.user_role.role.name
        == Role.ACCOUNT_ADMIN["name"]
    ) and current_user.account_id != account_id:
        raise HTTPException(
            status_code=401,
            detail=(
                "This user does not have the permissions to "
                "update this account"
            ),
        )
    account = crud.account.get(db, obj_id=account_id)
    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account does not exist",
        )
    return crud.account.update(db, db_obj=account, obj_in=account_in)


@router.post("/{account_id}/users/", response_model=schemas.User)
def add_user_to_account(
    *,
    db: Session = Depends(deps.get_db),
    account_id: str,
    user_id: str = Body(..., embed=True),
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[
            Role.ADMIN["name"],
            Role.SUPER_ADMIN["name"],
            Role.ACCOUNT_ADMIN["name"],
        ],
    ),
) -> Any:
    """
    Add a user to an account.
    """
    if current_user is None:
        raise exceptions.get_user_exception("user not found")
    account = crud.account.get(db, obj_id=account_id)
    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account does not exist",
        )
    user = crud.user.get(db, obj_id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User does not exist",
        )
    user_in = schemas.UserUpdate(account_id=account_id)
    return crud.user.update(db, db_obj=user, obj_in=user_in)


# TODO: remove account from user


@router.get(
    "/{account_id}/users/", response_model=List[schemas.User]
)
def retrieve_users_for_account(
    *,
    db: Session = Depends(deps.get_db),
    account_id: str,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Retrieve users for an account.
    """
    if current_user is None:
        raise exceptions.get_user_exception("user not found")
    account = crud.account.get(db, obj_id=account_id)
    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account does not exist",
        )
    return crud.user.get_by_account_id(db, account_id=account_id)


@router.get("/users/me/", response_model=List[schemas.Account])
def retrieve_users_with_own_account(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[
            Role.ADMIN["name"],
            Role.SUPER_ADMIN["name"],
            Role.ACCOUNT_ADMIN["name"],
        ],
    ),
) -> Any:
    """
    Retrieve users for my own account.
    """
    if current_user is None:
        raise exceptions.get_user_exception("user not found")
    account = crud.account.get(db, obj_id=current_user.account_id)
    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account does not exist",
        )
    return crud.user.get_by_account_id(db, account_id=account.id)
