from models import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, CHAR
from sqlalchemy import ForeignKey

class Customer(Base):
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True, nullable=False)
    order_ammount: Mapped[int] = mapped_column("orderAmmount", Integer(), nullable=False)
    person_id = Mapped[int] = mapped_column(ForeignKey("person.id"))
