from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, ForeignKey, Text
from sqlalchemy.orm import relationship

from entity.base import Base

class Track(Base):
    __tablename__ = 'track'
    track_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    spotify_id = Column(String(255), unique=True)
    album_id = Column(Integer, ForeignKey('album.album_id'))
    track_number = Column(Integer, nullable=False)
    spotify_popularity = Column(Integer, nullable=True)
    is_lyrics = Column(Boolean, default=False, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    album = relationship("Album", back_populates="tracks")
