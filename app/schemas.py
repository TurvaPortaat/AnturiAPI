#Pydantic honmia

from pydantic import BaseModel

# sanon täs ett tän malli on tämmäne jne..
class SensorCreate(BaseModel):
    identifier: str
    block_id: int
    status: str

class SensorUpdate(BaseModel)
    block_id: str
    status: str

class BlockCreate(BaseModel)
    name: str
    
class BlockUpdate(BaseModel)
    name: str