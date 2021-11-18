from sqlalchemy import create_engined
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = 'sqlite:///./data.db'

engine = create_engine(database_url, 
                       connect_args={"check_same_thread": False})

base = declarative_base()

session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)