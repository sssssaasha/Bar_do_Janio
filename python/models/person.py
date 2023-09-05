from models import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, CHAR

class Person(Base):
    __tablename__ = "person"
    id: Mapped[int] = mapped_column("id", Integer(), primary_key=True, autoincrement=True, nullable=False)
    cpf: Mapped[str] = mapped_column("cpf", CHAR(11), unique=True, nullable=False)
    rg: Mapped[str] = mapped_column("rg", VARCHAR(11), nullable=False)
    name: Mapped[str] = mapped_column("person_name", VARCHAR(256), nullable=False)
    
