from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class FormElement(Base):
    __tablename__ = "form_elements"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String, index=True, nullable=False
    )
    form_id = Column(
        Integer, ForeignKey("forms.id"), nullable=True
    )
    # TODO relationship
    form = relationship(
        "Form", back_populates="form_elements"
    )
    form_element_list_values = relationship(
        "FormElementListValue", back_populates="form_element"
    )
    form_element_types = relationship(
        "FormElementType", back_populates="form_element"
    )
    filled_forms = relationship(
        "FilledForm", back_populates="form_element"
    )    