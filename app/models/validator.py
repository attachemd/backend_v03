from sqlalchemy import (
    Column,
    Integer,
    String,
)
from app.db.base_class import Base


class Validator(Base):
    __tablename__ = "validators"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String, unique=True, index=True, nullable=False
    )
    