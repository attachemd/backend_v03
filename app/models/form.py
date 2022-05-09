from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Form(Base):
    __tablename__ = "forms"
    id = Column(Integer, primary_key=True, index=True)
    # FIXME name maybe deprecated
    # name = Column(String, unique=False, index=True, nullable=False)
    # TODO relationship
    form_element_fields = relationship("FormElementField")
    products = relationship("Product", back_populates="form")
