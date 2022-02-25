from typing import Any, List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from app import crud, exceptions, models, schemas
from app.api import deps
from app.constants.role import Role

router = APIRouter(prefix="/form_elements", tags=["form_elements"])

# ANCHOR Create a form element

@router.post("", response_model=schemas.FormElement)
def create_form_element(
    *,
    db: Session = Depends(deps.get_db),
    form_element_in: schemas.FormElementCreate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Create a form element.
    """
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")

    return crud.form_element.create(
        db, obj_in=form_element_in
    )

# Assign a form to a form element

# Assign a form element type to a for element

# Get all form elements

@router.get("", response_model=List[schemas.FormElement])
def get_all_form_elements(
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    # Get all form elements.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.form_element.get_multi(db)

# Update the form element

# Delete the form element if not used
