from typing import Any
from app import crud, models, schemas, exceptions
from app.constants.role import Role
from fastapi import APIRouter, Depends, Security, HTTPException
from sqlalchemy.orm import Session
from app.api import deps

router = APIRouter(
    prefix="/form_element_options",
    tags=["form_element_options"],
)

# Create a form element option one row at a time and
# assign a form element to it.
@router.post("", response_model=schemas.FormElementOption)
def create_form_element_option(
    *,
    db: Session = Depends(deps.get_db),
    form_element_option_in: schemas.FormElementOptionCreate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Create a form element option.
    """
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")

    return crud.form_element_option.create(
        db, obj_in=form_element_option_in
    )


# Update form element option.

# Delete a form element option.
@router.delete("/{form_element_option_id}")
def delete_form_element_option(
    *,
    form_element_option_id:str,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Delete a form element option.
    """
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")

    return crud.form_element_option.delete(
        db, obj_id=form_element_option_id
    )
    