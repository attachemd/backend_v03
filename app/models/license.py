import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class License(Base):
    __tablename__ = "licenses"
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(255), index=True)
    name = Column(String(100), index=True)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    simple_license = relationship(
        "SimpleLicense", back_populates="license", uselist=False
    )
    config_license = relationship(
        "ConfigLicense", back_populates="license", uselist=False
    )
