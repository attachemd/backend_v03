from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class SelectedListValue(Base):
    __tablename__ = "selected_list_values"
    id = Column(Integer, primary_key=True, index=True)
    filled_form_id = Column(
        Integer, ForeignKey("filled_forms.id"), nullable=False
    )
    form_element_list_value_id = Column(
        Integer,
        ForeignKey("form_element_list_values.id"),
        unique=True,
        nullable=False,
    )

    form_element_list_value = relationship("FormElementListValue")
