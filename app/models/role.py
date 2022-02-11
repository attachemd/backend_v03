from sqlalchemy import Column, Integer, String, Text

# from app.api import deps
# from app.models import Base
from app.db.base_class import Base


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(Text)
