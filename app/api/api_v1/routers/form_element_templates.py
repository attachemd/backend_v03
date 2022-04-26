from typing import Any, List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from app import crud, exceptions, models, schemas
from app.api import deps
from app.constants.role import Role

router = APIRouter(prefix="/form_element_templates", tags=["form_element_templates"])

# ANCHOR Create a form element template

@router.post("", response_model=schemas.FormElementTemplate)
def create_form_element_template(
    *,
    db: Session = Depends(deps.get_db),
    form_element_in: schemas.FormElementTemplateCreate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Create a form element template.
    """
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")

    return crud.form_element_template.create(
        db, obj_in=form_element_in
    )

# Assign a form to a form element template

# Assign a form element template type to a for element

# Get all form element templates

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

# Update the form element template

# Delete the form element template if not used
