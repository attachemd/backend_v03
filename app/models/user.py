import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

# from app.api import deps
from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), index=True)
    email = Column(
        String(100), unique=True, index=True, nullable=False
    )
    phone_number = Column(
        String(13), unique=True, index=True, nullable=True
    )
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    # account_id = Column(
    #     Integer, ForeignKey("accounts.id"), nullable=True
    # )

    user_role = relationship(
        "UserRole", back_populates="user", uselist=False
    )
