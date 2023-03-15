from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import consts

engine = create_engine(f'sqlite:///{consts.DATABASE_NAME}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

def create_db():
    Base.metadata.create_all(engine)

# class Logins(Base):
#     __tablename__ = "Logins"

#     username = Column(String, primary_key=True)
#     password = Column(String)

#     def tuple(self):
#         return (self.username, self.password)
#     def at(self, index: int):
#         return self.tuple()[index]

class Hotels(Base):
    __tablename__ = "Hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    region = Column(ForeignKey("Region.name"))

    def tuple(self):
        return (self.id, self.name, self.region)
    def at(self, index: int):
        return self.tuple()[index]
    
class Room_capacity(Base):
    __tablename__ = "Room_capacity"

    id = Column(String, primary_key=True)
    hotel = Column(ForeignKey("Hotels.id"))
    
    def tuple(self):
        return (self.id, self.hotel)
    def at(self, index: int):
        return self.tuple()[index]

    
class Room(Base):
    __tablename__ = "Room"

    id = Column(Integer, primary_key=True)
    hotel = Column(ForeignKey("Hotels.id"))
    number = Column(String(10))
    category = Column(String) #стандарт люкс апартамент
    seats = Column(Integer) # стандарт и люкс(до 2) апартамент(до 4) 
    status = Column(String) # занят, занят грязный, свободен чистый, свободен грязный

    
    def tuple(self):
        return (self.id, self.hotel, self.number, self.category, self.seats, self.status)
    def at(self, index: int):
        return self.tuple()[index]
    
class Busy(Base):
    __tablename__ = "Busy"

    id = Column(Integer, primary_key=True)
    number = Column(ForeignKey("Room.id"))
    start = Column(Date)
    end = Column(Date)
    
    def tuple(self):
        return (self.id, self.number, self.start, self.end)
    def at(self, index: int):
        return self.tuple()[index]

class Region(Base):
    __tablename__ = "Region"

    name = Column(String, primary_key=True)

    def tuple(self):
        return (self.name)
    def at(self, index: int):
        return self.tuple()[index]
