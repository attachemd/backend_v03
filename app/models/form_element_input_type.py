from sqlalchemy import (
    Column,
    Integer,
    String,
)
from app.db.base_class import Base


class FormElementInputType(Base):
    __tablename__ = "form_element_input_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String, unique=True, index=True, nullable=False
    )
    description = Column(
        String, unique=True, index=True, nullable=True
    )
    