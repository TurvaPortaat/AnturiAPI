from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager
from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI, Header, HTTPException, Depends
from .fake_db import users_db

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

engine = create_engine("sqlite:///./test.db") #jokuvaa tähä
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_user(token: str = Depends(oauth2_scheme)):
    return users_db.get(token)

@contextmanager
def db_session():
    """Dependancy for creating a new database session."""   #Lyhyt kuvaus mikä homma
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        


#Täs tämmöne blokki millä tarkistaisin käyttäjätunnistetiedot jokases reitis jos on autentikointii        
async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":  #joo oon tosi mielikuvituksellinen täs :D
        raise HTTPException(status_code=400, detail="X-token header invalid")
    
async def get_current_username(token: str= Depends(oauth2_scheme)):
    user = get_user(token)
    if not user:    #//paiskataa virheviesti jos typottaa
        raise HTTPException(status_code=404, detail="User not found")
    return user

#Voin antaa 85% varmuuden että tää toimis just jotenki näi :D 

#Korjasin tänne nyt importit tarkemmin että kaikki varmasti tulee mitä tarvii
