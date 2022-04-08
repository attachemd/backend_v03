from typing import List
from anyio import Any
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session

from app import crud, exceptions, models, schemas
from app.api import deps
from app.constants.role import Role

router = APIRouter(prefix="/products", tags=["products"])

# Create a product 

# Get product by id

@router.get("/{product_id}", response_model=schemas.Product)
async def get_product_by_id(
    product_id: str,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Get product by id.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.product.get(db, obj_id=product_id)

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
