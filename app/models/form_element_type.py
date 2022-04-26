from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class FormElementType(Base):
    __tablename__ = "form_element_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String, unique=True, index=True, nullable=False
    )
    
    # form_element_input_type_id = Column(
    #     Integer, ForeignKey("form_element_input_types.id"), nullable=True
    # )

    # TODO relationship
    
    form_element_input_type = relationship("FormElementInputType")
    