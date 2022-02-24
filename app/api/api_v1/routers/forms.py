from typing import Any, List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from app import crud, exceptions, models, schemas
from app.api import deps
from app.constants.role import Role

router = APIRouter(prefix="/forms", tags=["forms"])

# Create a form ANCHOR

# Get all forms ANCHOR[id=my-anchor]

@router.get("", response_model=List[schemas.Form])
def get_all_forms(
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    # Get all forms.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.form.get_multi(db)

# Update the form

# Delete the form if nothing assigned to it
