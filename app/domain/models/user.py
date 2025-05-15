from sqlalchemy import Column, BigInteger, String, Integer
from app.core.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    email = Column(String(255))
    name = Column(String(255))  
    password = Column(String(255))
    username = Column(String(255))
    image_url = Column(String(255))
    age = Column(Integer)
