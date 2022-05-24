from re import L
from typing import Any, List, Optional, Set
from fastapi import APIRouter, Depends, HTTPException, Security
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app import crud, exceptions, models, schemas
from app.api import deps
from app.constants.role import Role
from app.models.form_element_field import FormElementField
from app.models.form_element_option import FormElementOption
from app.models.selected_list_value import SelectedListValue

router = APIRouter(prefix="/forms", tags=["forms"])


class Option(BaseModel):
    url: str
    name: str


# Create a form ANCHOR


# @router.post("", response_model=schemas.Form)
@router.post("")
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

    # Assign new created form to the current product
    # Get Product by id
    if form_in.product_id:
        product_model = crud.product.get(
            db, obj_id=form_in.product_id
        )
        product_in = schemas.ProductUpdate(form_id=form.id)
        print("product_model")
        print(product_model)
        print("product_in")
        print(product_in)
        crud.product.update(
            db, db_obj=product_model, obj_in=product_in
        )
    else:
        raise HTTPException(
            status_code=404,
            detail="No product is provided",
        )
    # Create form element fields
    for form_element_field in form_in.form_element_fields:
        field_template = form_element_field.form_element_template
        form_element_field_in = schemas.FormElementFieldCreate(
            name=form_element_field.name,
            form_element_template_id=field_template.id,
            form_id=form.id,
            sort_id=form_element_field.sort_id,
        )
        form_element_field_model = crud.form_element_field.create(
            db, obj_in=form_element_field_in
        )

        # Delete form element options by form element field
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
                form_element_option_model = crud.form_element_option.create(
                    db, obj_in=form_element_option_in
                )
                # Create default list value for new created option
                selected_list_value_in = schemas.SelectedListValueCreate(
                    form_element_option_id=form_element_option_model.id,
                    form_element_field_id=form_element_field_model.id,
                    value="False",
                )
                crud.selected_list_value.create(
                    db, obj_in=selected_list_value_in
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

            # Check if selected value by form_element_field_id exists
            selected_value_model = (
                crud.selected_value.get_by_form_element_field_id(
                    db, form_element_field_id=form_element_field.id
                )
            )

            if selected_value_model:
                selected_value_in = schemas.SelectedValueUpdate(
                    form_element_field_id=form_element_field.id,
                    value=form_element_field.selected_value,
                )
                crud.selected_value.update(
                    db,
                    db_obj=selected_value_model,
                    obj_in=selected_value_in,
                )
            else:
                selected_value_in = schemas.SelectedValueCreate(
                    form_element_field_id=form_element_field.id,
                    value=form_element_field.selected_value,
                )
                crud.selected_value.create(
                    db, obj_in=selected_value_in
                )
                
        # FIXME get red of is not None
        if (
            form_element_field.selected_list_value_with_id
            is not None
        ):
            # print("selected_list_value")
            # print(form_element_field.selected_list_value)
            selected_list_value_update_vals = list()
            for (
                selected_list_value
            ) in form_element_field.selected_list_value_with_id:
                selected_list_value_update_vals.append(
                    {
                        "id": selected_list_value.id,  # This is pk?
                        "value": selected_list_value.value,
                    }
                )
                # # print(
                # #     key,
                # #     "->",
                # #     form_element_field.selected_list_value[key],
                # # )
                # option_id = get_option_id(
                #     form_element_field.form_element_options, key
                # )
                # # print()
                # selected_list_value_in = (
                #     schemas.SelectedListValueCreate(
                #         form_element_option_id=option_id,
                #         form_element_field_id=form_element_field.id,
                #         value=form_element_field.selected_list_value[
                #             key
                #         ],
                #     )
                # )
                # crud.selected_list_value.create(
                #     db, obj_in=selected_list_value_in
                # )
            db.bulk_update_mappings(
                SelectedListValue, selected_list_value_update_vals
            )
            db.commit()
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
@router.get("/{form_id}", response_model=schemas.Form)
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


# @router.put("/{form_id}", response_model=schemas.Form)
@router.put("/{form_id}")
def update_form(
    *,
    db: Session = Depends(deps.get_db),
    form_id: str,
    form_in: schemas.FormCreateForRoute,
    current_user: models.User = Security(
        deps.get_current_active_user,
        scopes=[
            Role.ADMIN["name"],
            Role.SUPER_ADMIN["name"],
        ],
    ),
) -> Any:
    """
    Update a form.
    """
    # my_new_posts = {1: "post1", 5: "post5", 1000: "post1000"}
    # print("my_new_posts.keys()")
    # if isinstance(form_in.deleted_option_ids, list):
    #     print("your object is a list !")
    # else:
    #     print("your object is not a list")
    # # print(form_in.deleted_option_ids.keys())
    # stmt = FormElementOption.__table__.delete().where(
    #     FormElementOption.id.in_(form_in.deleted_option_ids)
    # )
    # db.execute(stmt)
    # db.commit()
    # return
    if current_user is None:
        raise exceptions.get_user_exception()

    # check if the form exist
    form = crud.form.get(db, obj_id=form_id)
    if not form:
        raise HTTPException(
            status_code=404,
            detail="Form does not exist",
        )

    # Delete provided options by id
    if form_in.deleted_option_ids is not None:
        stmt = FormElementOption.__table__.delete().where(
            FormElementOption.id.in_(form_in.deleted_option_ids)
        )
        db.execute(stmt)
        db.commit()
    # Delete list value by option id
    for deleted_option_id in form_in.deleted_option_ids:
        crud.selected_list_value.delete_by_form_element_option_id(
            db,
            form_element_option_id=deleted_option_id,
        )
    # return crud.form.update(db, db_obj=form, obj_in=form_in)
    form_element_field_update_vals = []
    
    # loop through form element fields
    for form_element_field in form_in.form_element_fields:
        field_template = form_element_field.form_element_template
        # form_element_field_exist_model = crud.form_element_field.get(
        #     db, obj_id=form_element_field.id
        # )
        # return form_element_field_exist_model
        
        # create form element fields if it has the state new
        if form_element_field.state == "new":
            # if not form_element_field_exist_model:
            print("empty")
            form_element_field_in = schemas.FormElementFieldCreate(
                name=form_element_field.name,
                form_element_template_id=field_template.id,
                form_id=form.id,
                sort_id=form_element_field.sort_id,
            )
            form_element_field_model = (
                crud.form_element_field.create(
                    db, obj_in=form_element_field_in
                )
            )
            
            # create form element option if exist
            if form_element_field.form_element_options is not None:
                for (
                    form_element_option
                ) in form_element_field.form_element_options:
                    form_element_option_in = schemas.FormElementOptionCreate(
                        name=form_element_option.name,
                        form_element_field_id=form_element_field_model.id,
                        # form_element_field_id="20",
                    )
                    form_element_option_model = crud.form_element_option.create(
                        db, obj_in=form_element_option_in
                    )
                    # Create default list value for new created option
                    selected_list_value_in = schemas.SelectedListValueCreate(
                        form_element_option_id=form_element_option_model.id,
                        form_element_field_id=form_element_field.id,
                        value="False",
                    )
                    crud.selected_list_value.create(
                        db, obj_in=selected_list_value_in
                    )
                    
        # update form element fields if it has the state old
        elif form_element_field.state == "old":
            # List of dictionary including primary key
            # form_element_field_mappings = [{
            #     'id': form_element_field.id, # This is pk?
            #     'sort_id': form_element_field.sort_id,
            # }, ...]
            form_element_field_update_vals.append(
                {
                    "id": form_element_field.id,  # This is pk?
                    "sort_id": form_element_field.sort_id,
                    "name": form_element_field.name,
                }
            )

            # Update options
            if form_element_field.form_element_options is not None:
                for (
                    form_element_option
                ) in form_element_field.form_element_options:
                    # update form element option if it has the state edited
                    if form_element_option.state == "edited":
                        form_element_option_model = (
                            crud.form_element_option.get(
                                db, obj_id=form_element_option.id
                            )
                        )
                        if (
                            form_element_option_model is not None
                            and form_element_option_model.name
                            != form_element_option.name
                        ):
                            crud.form_element_option.update(
                                db,
                                db_obj=form_element_option_model,
                                obj_in=form_element_option,
                            )
                    # create form element option if it has the state new
                    if form_element_option.state == "new":
                        form_element_option_in = schemas.FormElementOptionCreate(
                            name=form_element_option.name,
                            form_element_field_id=form_element_field.id,
                            # form_element_field_id="20",
                        )
                        form_element_option_model = (
                            crud.form_element_option.create(
                                db, obj_in=form_element_option_in
                            )
                        )
                        # Create default list value for new created option
                        selected_list_value_in = schemas.SelectedListValueCreate(
                            form_element_option_id=form_element_option_model.id,
                            form_element_field_id=form_element_field.id,
                            value="False",
                        )
                        crud.selected_list_value.create(
                            db, obj_in=selected_list_value_in
                        )
            # # Create form element option for the form element field
            # if form_element_field.form_element_options is not None:
            #     # Delete form element options by form element field
            #     crud.form_element_option.delete_by_form_element_field_id(
            #         db,
            #         form_element_field_id=form_element_field.id,
            #     )
            #     for (
            #         form_element_option
            #     ) in form_element_field.form_element_options:
            #         form_element_option_in = schemas.FormElementOptionCreate(
            #             name=form_element_option.name,
            #             form_element_field_id=form_element_field.id,
            #         )
            #         crud.form_element_option.create(
            #             db, obj_in=form_element_option_in
            #         )

        elif form_element_field.state == "deleted":
            if form_element_field.form_element_options is not None:
                # Delete form element options by form element template
                crud.form_element_option.delete_by_form_element_field_id(
                    db,
                    form_element_field_id=form_element_field.id,
                )
            crud.form_element_field.delete(
                db, obj_id=form_element_field.id
            )
    db.bulk_update_mappings(
        FormElementField, form_element_field_update_vals
    )
    db.commit()

    return form
