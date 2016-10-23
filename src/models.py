from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
	__tablename__ = 'employee'
	id = Column(Integer, primary_key=True)
	fullname = Column(String(250), nullable=False)
	position = Column(String(250), nullable=False)
	pay = Column(String(250), nullable=False)