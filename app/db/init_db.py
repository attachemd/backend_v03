from sqlalchemy.orm import Session

from app import crud, schemas
from app.constants.role import Role
from app.core.config import settings


def init_db(db: Session) -> None:
    # Create Super Admin Account
    account = crud.account.get_by_name(
        db, name=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME
    )
    if not account:
        account_in = schemas.AccountCreate(
            # name=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME,
            name="superaccount",
            description="superadmin account",
        )
        crud.account.create(db, obj_in=account_in)

    # Create 1st Superuser
    user = crud.user.get_by_email(
        db, email=settings.FIRST_SUPER_ADMIN_EMAIL
    )
    if not user:
        account = crud.account.get_by_name(
            db, name=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME
        )
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPER_ADMIN_EMAIL,
            password=settings.FIRST_SUPER_ADMIN_PASSWORD,
            full_name=settings.FIRST_SUPER_ADMIN_EMAIL,
            account_id=account.id,
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
        print(role_name)
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
