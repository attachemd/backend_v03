from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from app.db.base_class import Base


class FilledForm(Base):
    __tablename__ = "filled_forms"
    id = Column(Integer, primary_key=True, index=True)
    form_element_id = Column(
        Integer, ForeignKey("form_elements.id"), nullable=True
    )
    value = Column(
        String, unique=True, index=True, nullable=False
    )
    # TODO relationship
