from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class SelectedValue(Base):
    __tablename__ = "selected_values"
    id = Column(Integer, primary_key=True, index=True)
    form_element_field_id = Column(
        Integer, ForeignKey("form_element_fields.id"), nullable=False
    )
    # client_id = Column(
    #     Integer, ForeignKey("clients.id"), nullable=False
    # )
    value = Column(
        String, index=True, nullable=True
    )
    # TODO relationship
    # form_element_template = relationship(
    #     "FormElementTemplate"
    # )   
    # selected_list_values = relationship(
    #     "SelectedListValue"
    # )