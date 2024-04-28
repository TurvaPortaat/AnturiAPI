from typing import Union
from fastapi import FastAPI
from fastapi import HTTPException

from fastapi import Depends
from .dependencies import db_session
from .dependencies import get_token_header, get_current_username


from . import crud, models, schemas
from .database import SessionLocal
from sqlalchemy.orm import Session
from models import Sensor #WIP 
from schemas import SensorCreate, SensorUpdate #WIP

#Kuinka monta importtii tähä viel keksis?

app = FastAPI()

#Täs tää käyttäjätietoje autentikointii homma juttu

@app.get("/users/me")
async def read_own_items(username: str = Depends(get_current_username)):
    return {"username":username}


@app.post("/items/")                            
def create_item(sensor: schemas.SensorCreate, db: Session = Depends(db_session)):
    return crud.create_sensor(db=db, sensor=sensor)
    
#Anturien hakua
@app.get("/sensors/", response_model=List[Sensor])
async def read_sensors():
    #TODO: Logiikka antureiden hakemiseen
    return sensors

@app.get("/sensors/{sensor_id}", response_model=Sensor)
async def read_sensors(sensor_id: int, db: Session = Depends(db_session)):
    sensor = crud.get_sensor(db, sensor_id=sensor_id)
    if sensor is None:  #//Jos ei oo sensorii ni paiskaa virhe
        raise HTTPException(status_code=404, detail="Sensor not found.")
    return sensor

#Anturien lisääminen, päivitys, poisto
@app.post("/sensors/", response_model=Sensor)
    #TODO: Logiikka uuden anturin luomiseen tietokantaan
    return new_sensor

# TODO hommia on vielä kasoittan täälläki D: fuufuu

@app.put("/sensors/{sensor_id}", response_model=Sensor)
async def update_sensor(sensor_id: int, sensor: SensorUpdate):
    #TODO: Logiikka anturin päivitykseen
    return updated_sensor

@app.delete("/sensors/{sensor_id}")
async def delete_sensor(sensor_id: int):
    #TODO: Logiikka anturin poistamiseen
    return {"message": "Sensor deleted"}


#Lohkohallinta
@app.post("/blocks/", response_model=Block)
async def create_block(block: BlockCreate):
    #TODO:Logiikka uuden lohkon luontiin
    return new_block

@app.put("/blocks/{block_id}", response_model=Block)
async def update_block(block_id: int, block: BlockUpdate):
    #TODO: Logiikka lohkon päivityksee
    return updated_block

@app.delete("/blocks/{block_id}")
async def delete_block(block_id: int):
    #TODO: Logiikka lohkon poistamisee
    return {"message:Block deleted"}

@app.get("/blocks/block_id}/sensors", response_model=LIST[Sensor])
async def read_block_sensors(block_id: int):
    #TODO: Logiikka tähä hakuhommaa
    return sensors_in_block