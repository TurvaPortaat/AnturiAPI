#Määritellään tietokantamallit
#Ekana importit niinku on opetettu
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship 
from sqlalchemy.ext.declarative import declarative_base

#Määritellää Base
Base = declarative_base()

#Luodaa Sensor ja Block -Baseclassit

class Sensor(Base):
    __tablename__ ="sensors"
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
