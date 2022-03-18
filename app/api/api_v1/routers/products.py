from typing import List
from anyio import Any
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session

from app import crud, exceptions, models, schemas
from app.api import deps
from app.constants.role import Role

router = APIRouter(prefix="/products", tags=["products"])

# Create a product 

# Get all products

@router.get("", response_model=List[schemas.Product])
def get_products(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Retrieve all products.
    """
    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")
    return crud.product.get_multi(db)

# Update the product

# Delete the product if nothing assigned to it
