from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BUser(Base):
    __tablename__ = 'b_user'
    id = Column(Integer, primary_key=True)
    created_at = Column(Time, primary_key=False)

