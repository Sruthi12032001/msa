from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    age = Column(Integer)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    address = Column(String)
    state = Column(String)
    pin_code = Column(Integer)
