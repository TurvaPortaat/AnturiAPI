from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime, timezone

Base = declarative_base()

class Sensor(Base):
    __tablename__ = 'sensors'
    id = Column(Integer, primary_key=True)
    identifier = Column(String, unique=True, nullable=False)
    block_id = Column(Integer, ForeignKey('blocks.id'))
    status = Column(String, nullable=False)
    measurements = relationship("Measurement", back_populates="sensor")
    
class Block(Base):
    __tablename__ = 'blocks'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    sensors = relationship("Sensor", back_populates="block")
    
class Measurement(Base):
    __tablename__ = 'measurements'
    id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer, ForeignKey('sensor.id'))
    temperature = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc)) # Datetimeen on asetettu lambdalla aikavyöhyketietoinen aikaleima
    sensor = relationship("Sensor", back_populates="measurements")

# Tietokantamoottori ja sessiot    
engine = create_engine('sqlite:///sensors.db')
Session = sessionmaker(bind=engine)
session = Session()

# Virhekäsittelyä ja taulujen luontia
try:
    Base.metadata.create_all(engine)
    print("Taulut luotu onnistuneesti")
except Exception as e:
    print("Virhe tauluja luodessa: ", e)