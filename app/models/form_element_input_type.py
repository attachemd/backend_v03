from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from app.db.base_class import Base


class FormElementInputType(Base):
    __tablename__ = "form_element_input_types"
    id = Column(Integer, primary_key=True, index=True)
    input_type = Column(
        String, unique=True, index=True, nullable=False
    )
    
    form_element_type_id = Column(
        Integer, ForeignKey("form_element_types.id"), nullable=False
    )
    