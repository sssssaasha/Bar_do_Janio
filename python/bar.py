from models import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR

class Bar(Base):
    __tablename__ = "bar"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column("bar_name", VARCHAR(100), nullable=False)
    phone: Mapped[str] = mapped_column("phone", VARCHAR(20), nullable=False)
    mail: Mapped[str] = mapped_column("mail", VARCHAR(45), nullable=False)