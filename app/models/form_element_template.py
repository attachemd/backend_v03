from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class FormElementTemplate(Base):
    __tablename__ = "form_element_templates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    # TODO dynamic list
    # form_id = Column(
    #     Integer, ForeignKey("forms.id"), nullable=True
    # )
    # TODO relationship
    # form = relationship(
    #     "Form", back_populates="form_element_templates"
    # )
    form_element_type_id = Column(
        Integer, ForeignKey("form_element_types.id"), nullable=True
    )

    # TODO relationship
    validations = relationship(
        "Validation",
    ) 

    form_element_type = relationship("FormElementType")
    # selected_values = relationship(
    #     "SelectedValue", back_populates="form_element_template"
    # )
    # form_element_options = relationship(
    #     "FormElementOption", back_populates="form_element_template"
    # )
