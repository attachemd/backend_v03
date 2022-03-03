from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class FilledForm(Base):
    __tablename__ = "filled_forms"
    id = Column(Integer, primary_key=True, index=True)
    form_element_id = Column(
        Integer, ForeignKey("form_elements.id"), nullable=False
    )
    account_id = Column(
        Integer, ForeignKey("accounts.id"), nullable=False
    )
    value = Column(
        String, index=True, nullable=True
    )
    # TODO relationship
    form_element = relationship(
        "FormElement"
    )   
    selected_list_values = relationship(
        "SelectedListValue"
    )