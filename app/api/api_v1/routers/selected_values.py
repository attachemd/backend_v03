from typing import Any, List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from app import crud, exceptions, models, schemas
from app.api import deps
from app.constants.role import Role


router = APIRouter(prefix="/selected_values", tags=["selected_values"])


# Assign a form element to selected value
@router.post("", response_model=schemas.SelectedValue)
def create_selected_value(
    *,
    db: Session = Depends(deps.get_db),
    selected_value_in: schemas.SelectedValueCreate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Assign a form element to selected value.
    """
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")

    return crud.selected_value.create(
        db, obj_in=selected_value_in
    )
    
# Get all selected values.
@router.get("", response_model=List[schemas.SelectedValue])
def get_all_selected_values(
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    # Get all selected values.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.selected_value.get_multi(db)


# Get a specific selected value by id.
@router.get("/{selected_value_id}", response_model=schemas.SelectedValue)
def get_user_by_id(
    selected_value_id: str,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific selected value by id.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.selected_value.get(db, obj_id=selected_value_id)


# Update the form element value

# Delete the form element value
