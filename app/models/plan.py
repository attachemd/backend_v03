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
    client_id = Column(
        Integer, ForeignKey("clients.id"), nullable=True
    )
    product_id = Column(
        Integer, ForeignKey("products.id"), nullable=True
    )
    product = relationship("Product", back_populates="plans")
    clients = relationship("Client", back_populates="plan")
