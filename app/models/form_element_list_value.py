from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base

# ANCHOR[id=FormElementListValue]
class FormElementListValue(Base):
    __tablename__ = "form_element_list_values"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String, unique=False, index=False, nullable=False)
    form_element_field_id = Column(
        Integer, ForeignKey("form_element_fields.id"), nullable=False
    ) 
    # TODO relationship
    form_element_template = relationship(
        "FormElementTemplate",
        back_populates="form_element_list_values",
    ) 
    