from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from entity.base import Base

class Album(Base):
    __tablename__ = 'album'
    album_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    album_type = Column(String(255))
    total_tracks = Column(Integer)
    spotify_id = Column(String(255), unique=True)
    cover_image = Column(String(255))
    release_date = Column(Date)

    artists = relationship("entity.ArtistAlbum.ArtistAlbum", back_populates="album")
    tracks = relationship("entity.Track.Track", back_populates="album")

