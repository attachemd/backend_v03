from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class CustomLicense(Base):
    __tablename__ = "custom_licenses"
    id = Column(Integer, primary_key=True, index=True)
    license_id = Column(
        Integer, ForeignKey("licenses.id"), nullable=True
    )
    form_id = Column(
        Integer, ForeignKey("forms.id"), nullable=True
    )
    license = relationship(
        "License", back_populates="custom_license", uselist=False
    )
