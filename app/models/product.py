from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String, unique=True, index=True, nullable=False
    )
    description = Column(
        Text, index=True, nullable=True
    )
    form_id = Column(
        Integer, ForeignKey("forms.id"), nullable=True
    )

    # plans = relationship("Plan", back_populates="product")
    licenses = relationship("License", back_populates="product")
    form = relationship("Form", back_populates="products")
    # custom_license = relationship(
    #     "CustomLicense", back_populates="product", uselist=False
    # )