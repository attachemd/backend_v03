from typing import Any, List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from app import crud, exceptions, models, schemas
from app.api import deps
from app.constants.role import Role

router = APIRouter(prefix="/form_element_templates", tags=["form_element_templates"])

# TODO Assign a form element to a form

# TODO Get all form element template

@router.get("", response_model=List[schemas.FormElementTemplate])
def get_all_form_element_templates(
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    # Get all form element templates.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.form_element_template.get_multi(db)

# TODO Update the form element template
