from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class HospitalCase(Base):
    __tablename__ = "hospital_cases"
    id = Column(Integer, primary_key=True, index=True)
    disease = Column(String, index=True)
    date = Column(Date, index=True)
    area_code = Column(String, index=True)
    cases = Column(Integer)

class EnvironmentRecord(Base):
    __tablename__ = "environment_records"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    area_code = Column(String, index=True)
    temperature = Column(Float)
    rainfall = Column(Float)
    humidity = Column(Float)
    population_density = Column(Float)