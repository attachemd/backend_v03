from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from app.db.base_class import Base


class FormElementListValue(Base):
    __tablename__ = "form_element_list_values"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String, unique=True, index=True, nullable=False
    )
    value = Column(
        String, unique=True, index=True, nullable=False
    )
    form_element_id = Column(
        Integer, ForeignKey("form_elements.id"), nullable=True
    )
