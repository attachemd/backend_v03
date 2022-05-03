from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Validation(Base):
    __tablename__ = "validations"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(
        String, unique=True, index=True, nullable=False
    )
    pattern = Column(
        String, unique=False, index=True, nullable=True
    )
    validator_id = Column(
        Integer,
        ForeignKey("validators.id"),
        unique=False,
        nullable=False,
    )
    form_element_template_id = Column(
        Integer,
        ForeignKey("form_element_templates.id"),
        unique=False,
        nullable=True,
    )
    form_element_field_id = Column(
        Integer,
        ForeignKey("form_element_fields.id"),
        unique=False,
        nullable=True,
    )
    validator = relationship(
        "Validator"
    )
    