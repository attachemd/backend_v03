from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from app.db.base_class import Base


class FormElement(Base):
    __tablename__ = "form_elements"
    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(
        Integer, ForeignKey("forms.id"), nullable=True
    )
    # TODO relationship
