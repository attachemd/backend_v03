from fastapi import APIRouter

from app.api.api_v1.routers import (
    form_element_fields,
    products,
    users,
    auth,
    roles,
    user_roles,
    clients,
    licenses,
    custom_licenses,
    simple_licenses,
    forms,
    form_element_templates,
    form_element_types,
    form_element_input_types,
    form_element_list_values,
    validations,
    validators,
    selected_list_values,
    filled_forms,
)

api_router = APIRouter(prefix="/api", tags=["api"])

api_router.include_router(auth.router)
api_router.include_router(licenses.router)
api_router.include_router(custom_licenses.router)
api_router.include_router(simple_licenses.router)
api_router.include_router(forms.router)
api_router.include_router(form_element_fields.router)
api_router.include_router(form_element_templates.router)
api_router.include_router(form_element_types.router)
api_router.include_router(form_element_input_types.router)
api_router.include_router(form_element_list_values.router)
api_router.include_router(validations.router)
api_router.include_router(validators.router)
api_router.include_router(selected_list_values.router)
api_router.include_router(filled_forms.router)
api_router.include_router(clients.router)
api_router.include_router(products.router)
api_router.include_router(users.router)
api_router.include_router(roles.router)
api_router.include_router(user_roles.router)
