#Lets Create, Read, Update, Delete with them database sensordatas
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from .models import Sensor
from .schemas import SensorCreate, SensorUpdate

def get_sensor(db: Session, sensor_id:int):
    return db.query(Sensor).filter(Sensor.id == sensor_id).first()

def get_sensors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Sensor).offset(skip).limit(limit).all()

def create_sensor(db:Session, sensor: SensorCreate):
    db_sensor=Sensor(**sensor.model_dump())
    try:
        db.add(db_sensor)
        db.commit()
        db.refresh(db_sensor)
        return db_sensor
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def update_sensor(db: Session, sensor_id: int, sensor: SensorUpdate):
    db_sensor=db.query(Sensor).filter(Sensor.id == sensor_id).first()
    if db_sensor:
        update_data = sensor.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_sensor, key, value)
        db.commit()
        db.refresh(db.sensor)
    return db_sensor

def delete_sensor(db:Session, sensor_id: int):
    db_sensor = db.query(Sensor).filter(Sensor.id == sensor_id).first()
    if db_sensor:
        db.delete(db_sensor)
        db.commit()
    return db_sensor