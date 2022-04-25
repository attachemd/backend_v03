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
        String, unique=True, index=True, nullable=True
    )
    validator_id = Column(
        Integer,
        ForeignKey("validators.id"),
        unique=True,
        nullable=False,
    )
    validator = relationship(
        "Validator"
    )
    