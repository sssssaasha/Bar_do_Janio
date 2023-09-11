from sqlalchemy import Column, Integer, ForeignKey
from models import Base

class BillingHasMethodOfPayment(Base):
    __tablename__ = "billing_has_method_of_payment"
    billing_id = Column(Integer, ForeignKey("Billing.id"), primary_key=True)
    method_of_payment_id = Column(Integer, ForeignKey("method_of_payment.Id"), primary_key=True)
