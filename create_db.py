from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import consts

engine = create_engine(f'sqlite:///{consts.DATABASE_NAME}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

def create_db():
    Base.metadata.create_all(engine)

class Отели(Base):
    '''self.id, self.название, self.регион'''
    __tablename__ = "Отели"

    id = Column(Integer, primary_key=True)
    название = Column(String(150))
    регион = Column(ForeignKey("Регионы.название"))

    def tuple(self):
        return (self.id, self.название, self.регион)

class Регионы(Base):
    '''self.название'''
    __tablename__ = "Регионы"

    название = Column(String, primary_key=True)

    def tuple(self):
        return (self.название)

class Номера(Base):
    '''self.номер, self.отель, self.категория, self.кол_во_мест, self.статус'''
    __tablename__ = "Номера"

    id = Column(Integer, primary_key=True)
    номер = Column(String(10))
    отель = Column(ForeignKey("Отели.id"))
    категория = Column(String)
    кол_во_мест = Column(String)
    статус = Column(String)
    дата_заезда = Column(Date)
    дата_выезда = Column(Date)

    def tuple(self):
        return (self.id, self.номер, self.отель, self.категория, self.кол_во_мест, self.статус, self.дата_заезда, self.дата_выезда)
