import datetime

from sqlalchemy import Column, String, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Client(Base):
    """
    Database model for an client
    """
    # TODO remove __tablename__
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), index=True, nullable=False)
    last_name = Column(String(255), index=True, nullable=False)
    email = Column(
        String(100), unique=True, index=True, nullable=False
    )
    phone_number = Column(
        String(13), unique=True, index=True, nullable=True
    )
    description = Column(String(255), nullable=True)
    country = Column(String(30), nullable=True)
    city = Column(String(30), nullable=True)
    is_active = Column(Boolean(), default=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    user_id = Column(
        Integer, ForeignKey("users.id"), nullable=False
    )

    user = relationship("User", back_populates="clients")
    plan = relationship("Plan", back_populates="clients")
    licenses = relationship("License", back_populates="client")
