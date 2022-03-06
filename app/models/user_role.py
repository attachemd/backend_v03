from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

# from app.api import deps
# from app.models import Base
from app.db.base_class import Base


class UserRole(Base):
    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=True)

    role = relationship("Role")
    user = relationship(
        "User", back_populates="user_roles"
    )

    # __table_args__ = (
    #     UniqueConstraint(
    #         "user_id", "role_id", name="unique_user_role"
    #     ),
    # )
