from typing import Any, List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from app import crud, exceptions, models, schemas
from app.api import deps
from app.constants.role import Role


router = APIRouter(prefix="/filled_forms", tags=["filled_forms"])


# Assign a form element to filled form
@router.post("", response_model=schemas.FilledForm)
def create_filled_form(
    *,
    db: Session = Depends(deps.get_db),
    filled_form_in: schemas.FilledFormCreate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Assign a form element to filled form.
    """
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")

    return crud.filled_form.create(
        db, obj_in=filled_form_in
    )
    
# Get all filled forms.
@router.get("", response_model=List[schemas.FilledForm])
def get_all_Filled_forms(
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    # Get all filled forms.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.filled_form.get_multi(db)


# Get a specific filled form by id.
@router.get("/{filled_form_id}", response_model=schemas.FilledForm)
def get_user_by_id(
    filled_form_id: str,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific filled form by id.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.filled_form.get(db, obj_id=filled_form_id)


# Update the form element value

# Delete the form element value
