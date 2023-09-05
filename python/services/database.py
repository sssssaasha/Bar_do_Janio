from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine 
from sqlalchemy.orm import Session
from urllib.parse import quote


instance: str = f'mysql+pymysql://root:{quote("Ann4L!nd@")}@localhost:3306/bar'

if not database_exists(instance):
    create_database(instance)

engine = create_engine(instance, echo=True)
session = Session(bind=engine, autocommit=False, autoflush=True)


