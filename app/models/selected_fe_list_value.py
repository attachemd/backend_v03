from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from app.db.base_class import Base


class SelectedFormElementListValue(Base):
    __tablename__ = "selected_form_element_list_values"
    id = Column(Integer, primary_key=True, index=True)
    form_element_list_value_id = Column(
        Integer, ForeignKey("form_element_list_values.id"), nullable=True
    )
    filled_form_id = Column(
        Integer, ForeignKey("filled_forms.id"), nullable=True
    )
    # TODO relationship
