from faker import Faker
from sqlalchemy.orm import Session
from app import crud, schemas

from app.constants.role import Role

fakegen = Faker()


def fake_data(db: Session) -> None:

    members = [
        attr
        for attr in dir(Role)
        if not callable(getattr(Role, attr))
        and not attr.startswith("__")
    ]
    for role_name in members:
        print(role_name)
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
