from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class ListValueFilledFormMTM(Base):
    __tablename__ = "list_value_filled_form_mtms"
    id = Column(Integer, primary_key=True, index=True)
    filled_form_id = Column(
        Integer, ForeignKey("filled_forms.id"), nullable=False
    )
    form_element_list_values_id = Column(
        Integer,
        ForeignKey("form_element_list_values.id"),
        nullable=False,
    )

    form_element_list_value = relationship("FormElementListValue")
