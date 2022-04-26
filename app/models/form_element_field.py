from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class FormElementField(Base):
    __tablename__ = "form_element_fields"
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, unique=False, index=True, nullable=False)
    form_id = Column(Integer, ForeignKey("forms.id"), nullable=False)
    form_element_template_id = Column(
        Integer, ForeignKey("form_element_templates.id"), nullable=False
    )

    form_element_template = relationship("FormElementTemplate")
