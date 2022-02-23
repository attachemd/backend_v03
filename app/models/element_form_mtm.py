from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class ElementFormMTM(Base):
    __tablename__ = "element_form_mtms"
    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("forms.id"), nullable=True)
    form_element_id = Column(
        Integer, ForeignKey("form_elements.id"), nullable=True
    )

    form_element = relationship("FormElement")
