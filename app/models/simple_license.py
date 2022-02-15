from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from app.db.base_class import Base


class SimpleLicense(Base):
    __tablename__ = "simple_licenses"
    id = Column(Integer, primary_key=True, index=True)
    app_name = Column(String(255), index=True)
    device_name = Column(String(255), index=True)
    license_id = Column(
        Integer, ForeignKey("licenses.id"), nullable=True
    )
