import datetime

from sqlalchemy import Column, String, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Account(Base):
    """
    Database model for an account
    """
    # TODO remove __tablename__
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
    description = Column(String(255))
    is_active = Column(Boolean(), default=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    user_id = Column(
        Integer, ForeignKey("users.id"), nullable=True
    )

    user = relationship("User", back_populates="accounts")
    plan = relationship("Plan", back_populates="accounts")
    licenses = relationship("License", back_populates="account")
