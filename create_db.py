from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import consts

engine = create_engine(f'sqlite:///{consts.DATABASE_NAME}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

def create_db():
    Base.metadata.create_all(engine)

class Logins(Base):
    __tablename__ = "Logins"

    username = Column(String, primary_key=True)
    password = Column(String)

    def tuple(self):
        return (self.username, self.password)
    def at(self, index: int):
        return self.tuple()[index]

class Hotels(Base):
    __tablename__ = "Hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    place = Column(String)

    def tuple(self):
        return (self.id, self.name, self.place)
    def at(self, index: int):
        return self.tuple()[index]

class Room(Base):
    __tablename__ = "Room"

    id = Column(Integer, primary_key=True)
    number = Column(String)
    floor = Column(String)

class Reservation(Base):
    __tablename__ = "Reservation"

    id = Column(Integer, primary_key=True)

