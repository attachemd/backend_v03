from typing import Any, List, Optional, Set
from fastapi import APIRouter, Depends, Security
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app import crud, exceptions, models, schemas
from app.api import deps
from app.constants.role import Role

router = APIRouter(prefix="/forms", tags=["forms"])

# Create a form ANCHOR

@router.post("", response_model=schemas.Form)
def create_form(
    *,
    db: Session = Depends(deps.get_db),
    form_in: schemas.FormCreate,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Create a form.
    """
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")

    return crud.form.create(
        db, obj_in=form_in
    )
    
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

class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []
    image: Optional[Image] = None


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
