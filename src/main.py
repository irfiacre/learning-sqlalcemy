from sqlalchemy import create_engine, Integer, String, Float, Column
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///mydatabase.db', echo=True)

Base = declarative_base()

class Person(Base):
    __tablename__='people'
    id=Column(Integer, primary_key=True)


