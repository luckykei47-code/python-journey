from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.orm import DeclarativeBase, Session

DATABASE_URL = "sqlite:///./sales.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread" : False})

class Base(DeclarativeBase):
    pass

class SaleModel(Base):
    __tablename__ = "sales"
    id = Column(String, primary_key = True)
    name = Column(String, nullable = False)
    price = Column(Float, nullable = False)

Base.metadata.create_all(bind= engine)