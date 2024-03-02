from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class MySQLManager:
    engine = create_engine('mysql+pymysql://root:1234@localhost:3306/song_data', echo=True)
    Session = sessionmaker(bind=engine)