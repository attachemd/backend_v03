from fastapi import APIRouter

from app.api.api_v1.routers import (
    element_form_mtms,
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
    selected_fe_list_values,
    form_element_list_values,
    list_value_filled_form_mtms,
    filled_forms,
)

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(licenses.router)
api_router.include_router(custom_licenses.router)
api_router.include_router(simple_licenses.router)
api_router.include_router(forms.router)
api_router.include_router(element_form_mtms.router)
api_router.include_router(form_elements.router)
api_router.include_router(form_element_types.router)
api_router.include_router(selected_fe_list_values.router)
api_router.include_router(form_element_list_values.router)
api_router.include_router(list_value_filled_form_mtms.router)
api_router.include_router(filled_forms.router)
api_router.include_router(accounts.router)
api_router.include_router(users.router)
api_router.include_router(roles.router)
api_router.include_router(user_roles.router)
