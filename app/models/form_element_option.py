from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base

# ANCHOR[id=FormElementOption]
class FormElementOption(Base):
    __tablename__ = "form_element_options"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=False, nullable=False)
    form_element_field_id = Column(
        Integer, ForeignKey("form_element_fields.id"), nullable=False
    ) 
    # TODO relationship
    # form_element_template = relationship(
    #     "FormElementTemplate",
    #     back_populates="form_element_options",
    # ) 
    
    # selected_option_value = relationship(
    #     "SelectedListValue", back_populates="form_element_option"
    # )
    # selected_option_value = relationship(
    #     "SelectedListValue"
    # )
    