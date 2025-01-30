#Pydantic honmia

from pydantic import BaseModel, constr, validator, Field

class SensorCreate(BaseModel):  #... = pakollinen, constr, rajoitettustr, Fieldissä regex ja min_length.
    identifier: constr= Field(..., regex=r"^\d{3}-\d{2}$") #Tyhmä constr ei meinannu laink toimii täs eka.
    block_id: int
    status: str
    
    @validator('block_id')
    def validate_block_id(clas, v):
        if v <= 0:
            raise ValueError('block_id must be greater than 0')

class SensorUpdate(BaseModel):
    block_id: int #Hups, täs oli aiemmin str jostain syystä?
    status: str

class BlockCreate(BaseModel):
    name: constr = Field(..., strip_whitespace=True, min_length=1)  #epätoivoisesti piti viel heittää Field välii lol
    
class BlockUpdate(BaseModel):
    name: str