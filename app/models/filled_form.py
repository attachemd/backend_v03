from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from app.db.base_class import Base


class ConfigLicense(Base):
    __tablename__ = "config_licenses"
    id = Column(Integer, primary_key=True, index=True)
    license_id = Column(
        Integer, ForeignKey("licenses.id"), nullable=True
    )
