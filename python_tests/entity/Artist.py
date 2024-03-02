from sqlalchemy import create_engine, Column, Integer, String, Date, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artist'
    artist_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    spotify_id = Column(String(255), nullable=True, unique=True)
    spotify_popularity = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())
