from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class FormElementField(Base):
    __tablename__ = "form_element_fields"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True, nullable=False)
    sort_id = Column(String, unique=False, nullable=False)
    form_id = Column(Integer, ForeignKey("forms.id"), nullable=False)
    form_element_template_id = Column(
        Integer, ForeignKey("form_element_templates.id"), nullable=False
    )

    form_element_template = relationship("FormElementTemplate")
    field_validations_overriding = relationship(
        "Validation",
    ) 
    
    form_element_options = relationship(
        "FormElementOption"
    )
    
    selected_value = relationship(
        "SelectedValue", uselist=False
    )
    selected_list_values = relationship(
        "SelectedListValue"
    )
