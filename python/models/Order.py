from sqlalchemy import Column, Integer, DECIMAL, ForeignKey
from models import Base

class Order(Base):
    __tablename__ = "Order"
    id_order = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    value = Column(DECIMAL(10, 2), nullable=False)
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=False)
    sale_id = Column(Integer, ForeignKey("Sale.Id"), nullable=False)
