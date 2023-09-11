from sqlalchemy import Column, Integer, ForeignKey
from models import Base

class OrderHasProduct(Base):
    __tablename__ = "Order_has_product"
    order_idorder = Column(Integer, ForeignKey("Order.id_order"), primary_key=True)
    order_employee_id = Column(Integer, ForeignKey("employee.id"))
    order_sale_id = Column(Integer, ForeignKey("Sale.Id"))
    product_id = Column(Integer, ForeignKey("Product.Id"))
