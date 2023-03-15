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
    имя = Column(String(150))
    регион = Column(ForeignKey("Region.name"))

    def tuple(self):
        return (self.id, self.имя, self.регион)
    def at(self, index: int):
        return self.tuple()[index]

class Room_capacity(Base):
    __tablename__ = "Room_capacity"

    id = Column(String, primary_key=True)
    отель = Column(ForeignKey("Hotels.id"))

    def tuple(self):
        return (self.id, self.отель)
    def at(self, index: int):
        return self.tuple()[index]


class Room(Base):
    __tablename__ = "Room"

    id = Column(Integer, primary_key=True)
    отель = Column(ForeignKey("Hotels.id"))
    номер = Column(String(10))
    категория = Column(String) #стандарт люкс апартамент
    места = Column(Integer) # стандарт и люкс(до 2) апартамент(до 4)
    статус = Column(String) # занят, занят грязный, свободен чистый, свободен грязный
    начало_брони = Column(String)
    конец_брони = Column(String)


    def tuple(self):
        return (self.id, self.отель, self.номер, self.категория, self.места, self.статус, self.начало_брони, self.конец_брони)
    def at(self, index: int):
        return self.tuple()[index]

class Region(Base):
    __tablename__ = "Region"

    имя = Column(String, primary_key=True)

    def tuple(self):
        return (self.имя)
    def at(self, index: int):
        return self.tuple()[index]


class Guests(Base):
    __tablename__ = "Guests"

    ФИО = Column(String(150))
    телефон = Column(String(12), primary_key=True)

    def tuple(self):
        return (self.телефон, self.ФИО)
    def at(self, index: int):
        return self.tuple()[index]

class Clients(Base):
    __tablename__ = "Clients"

    id = Column(Integer, primary_key=True)
    фио = Column(String(150))
    тип = Column(String) # физ лицо или юр лицо


    def tuple(self):
        return (self.id, self.фио, self.тип)
    def at(self, index: int):
        return self.tuple()[index]

class Reservation_log(Base):
    '''(self.id, self.date, self.client, self.hotel, self.room, self.start_date, self.end_date, self.price)'''
    __tablename__ = "Reservation_log"

    id = Column(Integer, primary_key=True)
    дата = Column(String)
    заказчик = Column(ForeignKey("Clients.id"))
    отель = Column(ForeignKey("Hotels.id"))
    комната = Column(ForeignKey("Room.id"))
    начало_брони = Column(String)
    конец_брони = Column(String)
    цена = Column(String)

    def tuple(self):
        return (self.id, self.дата, self.заказчик, self.отель, self.комната, self.начало_брони, self.конец_брони, self.цена)
    def at(self, index: int):
        return self.tuple()[index]

