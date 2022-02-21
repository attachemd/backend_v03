import random
import uuid
from faker import Faker
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app import crud, schemas

from app.constants.role import Role

fakegen = Faker()


def fake_data(db: Session) -> None:
    # Create user for each role except super admin
    members = [
        attr
        for attr in dir(Role)
        if not callable(getattr(Role, attr))
        and not attr.startswith("__")
    ]
    for role_name in members:
        if role_name != Role.SUPER_ADMIN["name"]:
            # Create user
            name = fakegen.name()
            first_name = name.split(" ")[0]
            last_name = " ".join(name.split(" ")[-1:])
            username = first_name[
                0
            ].lower() + last_name.lower().replace(" ", "")
            email = username + "@" + last_name.lower() + ".com"
            password = "1234"
            user_in = schemas.UserCreate(
                email=email,
                password=password,
                full_name=first_name + " " + last_name,
            )
            user = crud.user.create(db, obj_in=user_in)
            # Assign super_admin role to user
            user_role = crud.user_role.get_by_user_id(
                db, user_id=user.id
            )
            if not user_role:
                role = crud.role.get_by_name(
                    db, name=getattr(Role, role_name)["name"]
                )
                user_role_in = schemas.UserRoleCreate(
                    user_id=user.id, role_id=role.id
                )
                crud.user_role.create(db, obj_in=user_role_in)

    # Create licenses
    for _ in range(10):
        license_in = schemas.LicenseCreate(
            key=uuid.uuid4().hex,
            description=fakegen.sentence(),
            type=random.choice(["SIMPLE", "CUSTOM"]),
        )
        crud.license.create(db, obj_in=license_in)

    # Create products
    for _ in range(10):
        product_in = schemas.ProductCreate(
            name=fakegen.company(),
        )
        crud.product.create(db, obj_in=product_in)

    # Assign license to product
    for _ in range(10):
        i=_+1
        user_role_in = schemas.PlanCreate(
            license_id=str(i), product_id=str(i)
        )
        crud.plan.create(db, obj_in=user_role_in)

    # Create simple license
    all_license = crud.license.get_multi(db)
    obj_data = jsonable_encoder(all_license)
    for field in obj_data:
        print(field)
    for _ in range(10):
        print(fakegen.word())
        # simple_license_in = schemas.SimpleLicenseCreate(
        #     device_name=fakegen.word()
        # )
        
        # crud.simple_license.create(db, obj_in=simple_license_in)