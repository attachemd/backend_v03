import datetime
import enum

from sqlalchemy import Column, Integer, String, Text, DateTime, Enum
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class LicenseType(enum.Enum):
    SIMPLE = "SIMPLE"
    CUSTOM = "CUSTOM"


class License(Base):
    __tablename__ = "licenses"
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(255), index=True)
    name = Column(String(100), index=True)
    type = Column(Enum(LicenseType))
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    simple_license = relationship(
        "SimpleLicense"
    )
    custom_license = relationship(
        "CustomLicense"
    )
