from sqlalchemy import Column, Integer, Date, DateTime, ForeignKey
from models import Base

class Sale(Base):
    __tablename__ = "Sale"
    Id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    date = Column(Date, nullable=False)
    creation_date = Column(DateTime, nullable=False)
    customer_id = Column(Integer, ForeignKey("Customer.id"), nullable=False)
    billing_id = Column(Integer, nullable=False)
    employee_id = Column(Integer, nullable=False)
