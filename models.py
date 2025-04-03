import os
from sqlalchemy import create_engine, Column, String 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DB file path
DB_FILE = os.path.join(os.path.dirname(__file__), '..', 'spacescope.db')

# Create SQLite engine
engine = create_engine(f"sqlite:///{DB_FILE}")
Base = declarative_base()

class APOD(Base):
    __tablename__ = "astronomy_pictures"

    date = Column(String, primary_key=True)
    title = Column(String)
    explanation = Column(String)
    hdurl = Column(String)
    url = Column(String)

# Create tables
Base.metadata.create_all(engine)

# Session factory
Session = sessionmaker(bind=engine)
