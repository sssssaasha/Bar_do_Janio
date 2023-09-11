from sqlalchemy import Column, Integer, String, Date, ForeignKey
from models import Base

class evaluation(Base):
    __tablename__ = "evaluation"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    comment = Column(String(100))
    rating = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    bar_id = Column(Integer, ForeignKey("bar.id"), nullable=False)
