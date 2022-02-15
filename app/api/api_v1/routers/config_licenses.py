from fastapi import APIRouter

from app.models.config_license import ConfigLicense

router = APIRouter(prefix="/config_license", tags=["config_license"])
