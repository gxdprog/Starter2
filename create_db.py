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

class Отели(Base):
    __tablename__ = "Отели"

    id = Column(Integer, primary_key=True)
    имя = Column(String(150))
    регион = Column(ForeignKey("Регион.имя"))

    def tuple(self):
        return (self.id, self.имя, self.регион)
    def at(self, index: int):
        return self.tuple()[index]



class Комната(Base):
    __tablename__ = "Комната"

    id = Column(Integer, primary_key=True)
    отель = Column(ForeignKey("Отели.id"))
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

class Регион(Base):
    __tablename__ = "Регион"

    имя = Column(String, primary_key=True)

    def tuple(self):
        return (self.имя)
    def at(self, index: int):
        return self.tuple()[index]


class Гости(Base):
    __tablename__ = "Гости"

    фио = Column(String(150))
    телефон = Column(String(12), primary_key=True)
    группа = Column(ForeignKey("Группа.id"))

    def tuple(self):
        return (self.телефон, self.фио, self.группа)
    def at(self, index: int):
        return self.tuple()[index]

class Клиенты(Base):
    __tablename__ = "Клиенты"

    id = Column(Integer, primary_key=True)
    фио = Column(String(150))
    тип = Column(String) # физ лицо или юр лицо


    def tuple(self):
        return (self.id, self.фио, self.тип)
    def at(self, index: int):
        return self.tuple()[index]

class Журнал_бронирования(Base):
    '''(self.id, self.дата, self.заказчик, self.отель, self.комната, self.начало_брони, self.конец_брони, self.цена)'''
    __tablename__ = "Журнал_бронирования"

    id = Column(Integer, primary_key=True)
    дата = Column(String)
    заказчик = Column(ForeignKey("Клиенты.id"))
    отель = Column(ForeignKey("Отели.id"))
    комната = Column(ForeignKey("Комната.id"))
    начало_брони = Column(String)
    конец_брони = Column(String)
    цена = Column(String)

    def tuple(self):
        return (self.id, self.дата, self.заказчик, self.отель, self.комната, self.начало_брони, self.конец_брони, self.цена)
    def at(self, index: int):
        return self.tuple()[index]

class Заезд(Base):
    '''(self.id, self.дата, self.отель, self.номер, self.дата_выезда, self.группа_гостей)'''
    __tablename__ = "Заезд"

    id = Column(Integer, primary_key=True)
    бронь = Column(ForeignKey("Журнал_бронирования.id"))
    дата = Column(String)
    отель = Column(ForeignKey("Отели.id"))
    номер = Column(ForeignKey("Комната.id"))
    дата_заезда = Column(String)
    дата_выезда = Column(String)
    группа_гостей = Column(ForeignKey("Группа.id"))

    def tuple(self):
        return (self.id, self.бронь, self.дата, self.отель, self.номер, self.дата_заезда, self.дата_выезда, self.группа_гостей)
    def at(self, index: int):
        return self.tuple()[index]

class Группа(Base):
    __tablename__ = "Группа"

    id = Column(Integer, primary_key=True)

    def tuple(self):
        return (self.id)
    def at(self, index: int):
        return self.tuple()[index]
    
