from sqlalchemy import Column, Integer, String
from models import Base

class MethodOfPayment(Base):
    __tablename__ = "method_of_payment"
    Id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(45), nullable=False)
    description = Column(String(256))
