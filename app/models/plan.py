from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(
        Integer, ForeignKey("accounts.id"), nullable=True
    )
    product_id = Column(
        Integer, ForeignKey("products.id"), nullable=True
    )
    product = relationship("Product", back_populates="plans")
    account = relationship("Account", back_populates="plans")
