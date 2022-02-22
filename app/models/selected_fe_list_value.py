from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class SelectedFormElementListValue(Base):
    __tablename__ = "selected_form_element_list_values"
    id = Column(Integer, primary_key=True, index=True)
    # filled_form_id = Column(
    #     Integer, ForeignKey("filled_forms.id"), nullable=True
    # )
    # # TODO relationship
    # filled_form = relationship(
    #     "FilledForm",
    #     back_populates="selected_form_element_list_values",
    # )
    # form_element_list_values = relationship(
    #     "FormElementListValue",
    #     back_populates="selected_form_element_list_value",
    # )
