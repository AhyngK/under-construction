from sqlalchemy import Column, Integer, ForeignKey, Text, DECIMAL
from sqlalchemy.orm import relationship

from entity.base import Base

class Lyric(Base):
    __tablename__ = 'lyric'
    lyric_id = Column(Integer, primary_key=True, autoincrement=True)
    track_id = Column(Integer, ForeignKey('track.track_id'), nullable=False)
    start_time = Column(DECIMAL(10, 3), nullable=False)
    end_time = Column(DECIMAL(10, 3), nullable=False)
    content = Column(Text, nullable=False)

    track = relationship("Track", back_populates="lyrics")
