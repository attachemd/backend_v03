from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class SimpleLicense(Base):
    __tablename__ = "simple_licenses"
    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String(255), index=True)
    # license_id = Column(
    #     Integer, ForeignKey("licenses.id"), nullable=True
    # )
    # license = relationship(
    #     "License", back_populates="simple_license", uselist=False
    # )
