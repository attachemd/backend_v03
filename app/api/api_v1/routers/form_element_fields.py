from typing import Any, List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from app import crud, exceptions, models, schemas
from app.api import deps
from app.constants.role import Role

router = APIRouter(prefix="/form_element_fields", tags=["form_element_fields"])

# TODO Assign a form element to a form

# TODO Get all form element field

@router.get("", response_model=List[schemas.FormElementField])
def get_all_form_element_fields(
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    # Get all form element fields.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.form_element_field.get_multi(db)

# TODO Update the form element field
