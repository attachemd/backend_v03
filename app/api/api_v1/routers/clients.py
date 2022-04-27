from typing import List, Any
from app import crud, models, schemas, exceptions
from app.constants.role import Role
from fastapi import APIRouter, Depends, Security, HTTPException, Body
from sqlalchemy.orm import Session

from app.api import deps

router = APIRouter(prefix="/clients", tags=["clients"])


@router.get("", response_model=List[schemas.Client])
def get_clients(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Retrieve all clients.
    """
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")
    return crud.client.get_multi(db)


# @router.get("/me", response_model=schemas.Client)
# def get_client_for_user(
#     *,
#     db: Session = Depends(deps.get_db),
#     current_user: models.User = Depends(
#         deps.get_current_active_user
#     ),
# ) -> Any:
#     """
#     Retrieve client for a logged in user.
#     """
#     # TODO[epic=exemple] redundant check
#     # LINK app\main.py#index
#     if current_user is None:
#         raise exceptions.get_user_exception("user not found")
#     return crud.client.get(db, obj_id=current_user.client_id)


@router.post("", response_model=schemas.Client)
def create_client(
    *,
    db: Session = Depends(deps.get_db),
    client_in: schemas.ClientCreate,
    current_user: models.User = Depends(
        deps.get_current_active_user
    ),
) -> Any:
    """
    Create an user client
    """
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")
    # Check if client name already exists
    client = crud.client.get_by_name(db, name=client_in.name)
    if client:
        raise HTTPException(
            status_code=409,
            detail="A client with this name already exists",
        )
    return crud.client.create(db, obj_in=client_in)


@router.put("/{client_id}", response_model=schemas.Client)
def update_client(
    *,
    db: Session = Depends(deps.get_db),
    client_id: str,
    client_in: schemas.ClientUpdate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[
            Role.ADMIN["name"],
            Role.SUPER_ADMIN["name"],
            Role.CLIENT_ADMIN["name"],
        ],
    ),
) -> Any:
    """
    Update an client.
    """

    # If user is an client admin,
    # check ensure they update their own client.
    # TODO update_client
    if (
        current_user.user_role.role.name
        == Role.CLIENT_ADMIN["name"]
    ) and current_user.client_id != client_id:
        raise HTTPException(
            status_code=401,
            detail=(
                "This user does not have the permissions to "
                "update this client"
            ),
        )
    client = crud.client.get(db, obj_id=client_id)
    if not client:
        raise HTTPException(
            status_code=404,
            detail="Client does not exist",
        )
    return crud.client.update(db, db_obj=client, obj_in=client_in)


# @router.post("/{client_id}/users", response_model=schemas.User)
# def add_user_to_client(
#     *,
#     db: Session = Depends(deps.get_db),
#     client_id: str,
#     user_id: str = Body(..., embed=True),
#     current_user: models.User = Security(
#         deps.get_current_active_user,
#         scopes=[
#             Role.ADMIN["name"],
#             Role.SUPER_ADMIN["name"],
#             Role.CLIENT_ADMIN["name"],
#         ],
#     ),
# ) -> Any:
#     """
#     Add a user to an client.
#     """
#     if current_user is None:
#         raise exceptions.get_user_exception("user not found")
#     client = crud.client.get(db, obj_id=client_id)
#     if not client:
#         raise HTTPException(
#             status_code=404,
#             detail="Client does not exist",
#         )
#     user = crud.user.get(db, obj_id=user_id)
#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="User does not exist",
#         )
#     user_in = schemas.UserUpdate(client_id=client_id)
#     return crud.user.update(db, db_obj=user, obj_in=user_in)


# TODO: remove client from user


# @router.get(
#     "/{client_id}/users", response_model=List[schemas.User]
# )
# def retrieve_users_for_client(
#     *,
#     db: Session = Depends(deps.get_db),
#     client_id: str,
#     current_user: models.User = Security(
#         deps.get_current_active_user,
#         scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
#     ),
# ) -> Any:
#     """
#     Retrieve users for an client.
#     """
#     if current_user is None:
#         raise exceptions.get_user_exception("user not found")
#     client = crud.client.get(db, obj_id=client_id)
#     if not client:
#         raise HTTPException(
#             status_code=404,
#             detail="Client does not exist",
#         )
#     return crud.user.get_by_client_id(db, client_id=client_id)


# @router.get("/users/me", response_model=List[schemas.Client])
# def retrieve_users_with_own_client(
#     *,
#     db: Session = Depends(deps.get_db),
#     current_user: models.User = Security(
#         deps.get_current_active_user,
#         scopes=[
#             Role.ADMIN["name"],
#             Role.SUPER_ADMIN["name"],
#             Role.CLIENT_ADMIN["name"],
#         ],
#     ),
# ) -> Any:
#     """
#     Retrieve users for my own client.
#     """
#     if current_user is None:
#         raise exceptions.get_user_exception("user not found")
#     client = crud.client.get(db, obj_id=current_user.client_id)
#     if not client:
#         raise HTTPException(
#             status_code=404,
#             detail="Client does not exist",
#         )
#     return crud.user.get_by_client_id(db, client_id=client.id)
