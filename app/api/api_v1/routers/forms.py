from typing import Any, List, Optional, Set
from fastapi import APIRouter, Depends, HTTPException, Security
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app import crud, exceptions, models, schemas
from app.api import deps
from app.constants.role import Role

router = APIRouter(prefix="/forms", tags=["forms"])


class Option(BaseModel):
    url: str
    name: str


# Create a form ANCHOR


@router.post("", response_model=schemas.Form)
# @router.post("")
def create_form(
    *,
    db: Session = Depends(deps.get_db),
    form_in: schemas.FormCreateForRoute,
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
    # Check if form name already exists
    # form_with_name = crud.form.get_by_name(db, name=form_in.name)
    # if form_with_name:
    #     raise HTTPException(
    #         status_code=409,
    #         detail="A form with this name already exists",
    #     )
    # Create a form
    # new_form_in = schemas.FormCreate(name=form_in.name)
    new_form_in = schemas.FormCreate()
    form = crud.form.create(db, obj_in=new_form_in)

    # Create form element fields
    for form_element_field in form_in.form_element_fields:
        field_template = form_element_field.form_element_template
        form_element_field_in = schemas.FormElementFieldCreate(
            name=form_element_field.name,
            form_element_template_id=field_template.id,
            form_id=form.id,
        )
        form_element_field_model = crud.form_element_field.create(
            db, obj_in=form_element_field_in
        )

        # Delete form element options by form element template
        # crud.form_element_option.delete_by_form_element_field_id(
        #     db,
        #     form_element_field_id=form_element_field.id,
        # )
        # Create form element option for the form element field
        if form_element_field.form_element_options is not None:
            for (
                form_element_option
            ) in form_element_field.form_element_options:
                form_element_option_in = schemas.FormElementOptionCreate(
                    name=form_element_option.name,
                    form_element_field_id=form_element_field_model.id,
                    # form_element_field_id="20",
                )
                crud.form_element_option.create(
                    db, obj_in=form_element_option_in
                )
    return form
    # return crud.form.create(
    #     db, obj_in=form_in
    # )
    # results = {"form_in": form_in}
    # return results


# @router.post("/fill_form", response_model=schemas.Form)
@router.post("/fill_form")
# @router.post("")
def fill_form(
    *,
    db: Session = Depends(deps.get_db),
    form_in: schemas.FormCreateForRoute,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
) -> Any:
    """
    Fill the form.
    """

    def get_option_id(options, name):
        if options is not None:
            # print("options")
            # print(options)
            for item in options:
                if item.name == name:
                    # return 
                    # print("item.name")
                    # print(item.name)
                    # print("item.id")
                    # print(item.id)
                    return item.id

    # TODO redundant check
    if current_user is None:
        raise exceptions.get_user_exception("user not found")

    # Create selected value for the form
    for form_element_field in form_in.form_element_fields:
        # if form_element_field.form_element_options is not None:
        #     print("form_element_options")
        #     print(form_element_field.form_element_options)
        #     get_option_id(form_element_field.form_element_options)
            # for item in form_element_field.form_element_options:
            #     print("item.name")
            #     print(item.name)
        if form_element_field.selected_value is not None:
            # print("selected_value")
            # print(form_element_field.selected_value)
            selected_value_in = (
                schemas.SelectedValueCreate(
                    form_element_field_id=form_element_field.id,
                    value=form_element_field.selected_value,
                )
            )
            crud.selected_value.create(
                db, obj_in=selected_value_in
            )
        if form_element_field.selected_list_value is not None:
            # print("selected_list_value")
            # print(form_element_field.selected_list_value)
            for key in form_element_field.selected_list_value:
                # print(
                #     key,
                #     "->",
                #     form_element_field.selected_list_value[key],
                # )
                option_id = get_option_id(form_element_field.form_element_options, key)
                # print()
                selected_list_value_in = schemas.SelectedListValueCreate(
                    form_element_option_id=option_id,
                    form_element_field_id=form_element_field.id,
                    value=form_element_field.selected_list_value[key]
                )
                crud.selected_list_value.create(
                    db, obj_in=selected_list_value_in
                )

    return "ok"


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


# Get form by id
@router.get("/by_id/{form_id}", response_model=schemas.Form)
def get_form_by_id(
    form_id=str,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    # Get form by id.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    return crud.form.get(db, obj_id=form_id)


# Get form by name
@router.get("/by_name/{form_name}", response_model=schemas.Form)
def get_form_by_name(
    form_name=str,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
    ),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    # Get form by name.
    """
    if current_user is None:
        raise exceptions.get_user_exception()
    form = crud.form.get_by_name(db, name=form_name)
    print("form")
    print(form)
    return form


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
