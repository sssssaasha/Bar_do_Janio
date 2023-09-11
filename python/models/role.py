from sqlalchemy import Column, Integer, String
from models import Base

class role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    description = Column(String(256))
    name = Column(String(45))
