from sqlalchemy import Column, Integer, DECIMAL, Date
from models import Base

class Billing(Base):
    __tablename__ = "billing"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    value = Column(DECIMAL(10, 2), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(Integer, nullable=False)
