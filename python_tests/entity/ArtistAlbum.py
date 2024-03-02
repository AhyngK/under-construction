from sqlalchemy import Column, Integer, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ArtistAlbum(Base):
    __tablename__ = 'artist_album'
    artist_id = Column(Integer, ForeignKey('artist.artist_id'), primary_key=True)
    album_id = Column(Integer, ForeignKey('album.album_id'), primary_key=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())
    # 관계 설정 (선택적)

    artist = relationship("Artist", back_populates="albums")
    album = relationship("Album", back_populates="artists")
