from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager
from fastapi import Header, HTTPException, Security

engine = create_engine("sqlite:///./test.db") #jokuvaa tähä
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def db_session():
    """Dependancy for creating a new database session."""   #Lyhyt kuvaus mikä homma
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        
def get_db():
    db=SessionLocal
    try:
        yield db
    finally:
        db.close_all()
        


#Täs tämmöne blokki millä tarkistaisin käyttäjätunnistetiedot jokases reitis jos on autentikointii        
async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":  #joo oon tosi mielikuvituksellinen täs :D
        raise HTTPException(status_code=400, detail="X-token header invalid")
    
async def get_current_username(credentials: HTTPBasicCredentials= Security(security)):
    if credentials.username not in fake_users_db: #Jos nää tosi aidot käyttäjätiedot ei oo tosiaidossa käyttäjätietokannas ni
        raise HTTPException(status_code=400, detail="Invalid authentication")
    return credentials.username

#Voin antaa 85% varmuuden että tää toimis just jotenki näi :D 
#Mainissa lisää
