from unicodedata import category
from database import Base
from sqlalchemy import Column, Float, ForeignKey,Integer,String,DateTime,func

class Users(Base):
    __tablename__="userstable"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True)
    email=Column(String,unique=True)
    hash_password=Column(String)

class Todos(Base):
    __tablename__="todostable"

    id=Column(Integer,primary_key=True)
    title=Column(String)
    amount=Column(Float)
    type=Column(String)
    category=Column(String)
    date=Column(DateTime(timezone=True),server_default=func.now())
    owner_id=Column(Integer,ForeignKey('userstable.id'))