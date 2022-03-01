from fastapi import APIRouter

from app.api.api_v1.routers import (
    form_element_templates,
    users,
    auth,
    roles,
    user_roles,
    accounts,
    licenses,
    custom_licenses,
    simple_licenses,
    forms,
    form_elements,
    form_element_types,
    form_element_list_values,
    selected_list_values,
    filled_forms,
)

api_router = APIRouter(prefix="/api", tags=["api"])

api_router.include_router(auth.router)
api_router.include_router(licenses.router)
api_router.include_router(custom_licenses.router)
api_router.include_router(simple_licenses.router)
api_router.include_router(forms.router)
api_router.include_router(form_element_templates.router)
api_router.include_router(form_elements.router)
api_router.include_router(form_element_types.router)
api_router.include_router(form_element_list_values.router)
api_router.include_router(selected_list_values.router)
api_router.include_router(filled_forms.router)
api_router.include_router(accounts.router)
api_router.include_router(users.router)
api_router.include_router(roles.router)
api_router.include_router(user_roles.router)
