from sqlalchemy import Column, Integer, DECIMAL, String, ForeignKey
from models import Base

class product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    value = Column(DECIMAL(10, 2), nullable=False)
    name = Column(String(45))
    description = Column(String(256))
    productcol = Column(String(45))
    order_employee_role_id = Column(Integer, ForeignKey("role.id"))
