from sqlalchemy import Column, Integer, Float, ForeignKey
from models import Base

class employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    salary = Column(Float, nullable=False)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)
