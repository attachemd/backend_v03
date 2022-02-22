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
    value = Column(String, unique=True, index=True, nullable=False)
    form_element_id = Column(
        Integer, ForeignKey("form_elements.id"), nullable=True
    )
    filled_form_id = Column(
        Integer,
        ForeignKey("filled_forms.id"),
        nullable=True,
    )   
    # TODO relationship
    form_element = relationship(
        "FormElement",
        back_populates="form_element_list_values",
    )
    filled_form = relationship(
        "FilledForm",
        back_populates="form_element_list_values",
    )   
