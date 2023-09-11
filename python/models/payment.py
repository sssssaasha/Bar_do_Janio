from sqlalchemy import Column, Integer, DECIMAL, String, ForeignKey
from models import Base

class payment(Base):
    __tablename__ = "payment"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    value = Column(DECIMAL(10, 2), nullable=False)
    description = Column(String(256))
    name = Column(String(45))
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)
