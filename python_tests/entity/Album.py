from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Album(Base):
    __tablename__ = 'album'
    album_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    album_type = Column(String(255))
    total_tracks = Column(Integer)
    spotify_id = Column(String(255))
    cover_image = Column(String(255))
    release_date = Column(Date)
