from typing import Any, List
from app import crud, models, schemas, exceptions
from app.constants.role import Role
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from app.api import deps

router = APIRouter(prefix="/selected_list_values", tags=["selected_list_values"])

# TODO Selecte a list value
@router.post("", response_model=schemas.SelectedListValue)
def create_selected_list_value(
    *,
    db: Session = Depends(deps.get_db),
    selected_list_value_in: schemas.SelectedListValueCreate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Selecte a list value.
    """
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")
    # FIXME raise exception for selecting list value mutiple time
    return crud.selected_list_value.create(
        db, obj_in=selected_list_value_in
    )

# TODO Get all selected list values
@router.get("", response_model=List[schemas.SelectedListValue])
def get_all_selected_list_values(
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    # Get all selected list values.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.selected_list_value.get_multi(db)

# TODO Update the selected_list_value
