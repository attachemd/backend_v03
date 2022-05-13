from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class SelectedListValue(Base):
    __tablename__ = "selected_list_values"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(
        String, index=True, nullable=True
    )
    # selected_value_id = Column(
    #     Integer, ForeignKey("selected_values.id"), nullable=False
    # )
    form_element_field_id = Column(
        Integer, ForeignKey("form_element_fields.id"), nullable=False
    )
    form_element_option_id = Column(
        Integer,
        ForeignKey("form_element_options.id"),
        unique=True,
        nullable=False,
    )

    form_element_option = relationship("FormElementOption")
