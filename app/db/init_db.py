from sqlalchemy.orm import Session
from app import crud, schemas
from app.constants.role import Role
from app.core.config import settings
from inspect import currentframe, getframeinfo

frameinfo = getframeinfo(currentframe())
cf = currentframe()
filename = getframeinfo(cf).filename
def get_linenumber():
    cf = currentframe()
    return cf.f_back.f_lineno

def init_db(db: Session) -> None:
    # # Create Super Admin Client
    # client = crud.client.get_by_name(
    #     db, name=settings.FIRST_SUPER_ADMIN_CLIENT_NAME
    # )
    # if not client:
    #     client_in = schemas.ClientCreate(
    #         # name=settings.FIRST_SUPER_ADMIN_CLIENT_NAME,
    #         name="superclient",
    #         description="superadmin client",
    #     )
    #     crud.client.create(db, obj_in=client_in)

    # Create 1st Superuser
    user = crud.user.get_by_email(
        db, email=settings.FIRST_SUPER_ADMIN_EMAIL
    )
    if not user:
        # client = crud.client.get_by_name(
        #     db, name=settings.FIRST_SUPER_ADMIN_CLIENT_NAME
        # )
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPER_ADMIN_EMAIL,
            password=settings.FIRST_SUPER_ADMIN_PASSWORD,
            full_name=settings.FIRST_SUPER_ADMIN_EMAIL,
            # client_id=client.id,
        )
        user = crud.user.create(db, obj_in=user_in)

    # Create Role If They Don't Exist
    members = [
        attr
        for attr in dir(Role)
        if not callable(getattr(Role, attr))
        and not attr.startswith("__")
    ]
    for role_name in members:
        # print(role_name, ":   ", filename, get_linenumber())
        role = crud.role.get_by_name(
            db, name=getattr(Role, role_name)["name"]
        )
        if not role:
            role_in = schemas.RoleCreate(
                name=getattr(Role, role_name)["name"],
                description=getattr(Role, role_name)["description"],
            )
            crud.role.create(db, obj_in=role_in)

    # Assign super_admin role to user
    user_role = crud.user_role.get_by_user_id(db, user_id=user.id)
    if not user_role:
        role = crud.role.get_by_name(
            db, name=Role.SUPER_ADMIN["name"]
        )
        user_role_in = schemas.UserRoleCreate(
            user_id=user.id, role_id=role.id
        )
        crud.user_role.create(db, obj_in=user_role_in)
