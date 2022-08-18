from sqlalchemy import Integer, Column, String
# from controller import Base
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'api_user'
    uid = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(30))
    lastname = Column(String(30))

