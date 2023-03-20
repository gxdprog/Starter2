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
    направление = Column(String)
    начало_мертвого_сезона = Column(Date)
    конец_мертвого_сезона = Column(Date)


    def tuple(self):
        return (self.id, self.название, self.регион, self.направление, self.начало_мертвого_сезона, self.конец_мертвого_сезона)

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
    группа_гостей = Column(ForeignKey("Списки_гостей.группа"))

    def tuple(self):
        return (self.id, self.номер, self.отель, self.категория, self.кол_во_мест, self.статус,
                self.дата_заезда, self.дата_выезда, self.группа_гостей)

class Гости(Base):
    __tablename__ = "Гости"

    телефон = Column(String(17), primary_key=True)
    фио = Column(String)
    группа = Column(ForeignKey("Списки_гостей.группа"))

    def tuple(self):
        return (self.телефон, self.фио, self.группа)

class Клиенты(Base):
    __tablename__ = "Клиенты"

    id = Column(Integer, primary_key=True)
    плательщик = Column(String(150))
    вид_плательщика = Column(String)

    def tuple(self):
        return (self.id, self.плательщик, self.вид_плательщика)

class Журнал_бронирования(Base):
    '''(self.id, self.дата, self.заказчик, self.отель, self.номер, self.дата_заезда, self.дата_выезда)'''
    __tablename__ = "Журнал_бронирования"

    id = Column(Integer, primary_key=True)
    дата = Column(Date)
    заказчик = Column(ForeignKey("Клиенты.id"))
    отель = Column(ForeignKey("Отели.id"))
    номер = Column(ForeignKey("Номера.id"))
    дата_заезда = Column(Date)
    дата_выезда = Column(Date)
    цена = Column(Float)

    def tuple(self):
        return (self.id, self.дата, self.заказчик, self.отель, self.номер, self.дата_заезда, self.дата_выезда, self.цена)

class Списки_гостей(Base):
    __tablename__ = "Списки_гостей"

    группа = Column(Integer, primary_key=True)

    def tuple(self):
        return (self.группа)


class Цены(Base):
    __tablename__ = "Цены"

    id = Column(Integer, primary_key=True)
    отель = Column(ForeignKey("Отели.id"))
    категория = Column(String)
    цена = Column(Float)

    def tuple(self):
        return (self.id, self.отель, self.категория, self.цена)

class Изменения_цен(Base):
    __tablename__ = "Изменения_цен"

    id = Column(Integer, primary_key=True)
    дата = Column(Date)
    отель = Column(ForeignKey("Отели.id"))
    категория = Column(String)
    цена = Column(Float)

    def tuple(self):
        return (self.id, self.дата, self.отель, self.категория, self.цена)

class Сотрудники(Base):
    '''self.id, self.фио_сотрудника, self.категория, self.вид_работ'''
    __tablename__ = "Сотрудники"

    id = Column(Integer, primary_key=True)
    фио_сотрудника = Column(String(150))
    вид_работ = Column(ForeignKey("Виды_работ.наименование"))

    def tuple(self):
        return (self.id, self.фио_сотрудника, self.вид_работ)


class Виды_работ(Base):
    __tablename__ = "Виды_работ"

    наименование = Column(String, primary_key=True)

    def tuple(self):
        return (self.наименование)

class Работа(Base):
    '''self.id, self.дата, self.фио_горничной, self.отель, self.номер_к_уборке, self.статус'''
    __tablename__ = "Работа"

    id = Column(Integer, primary_key=True)
    дата = Column(Date)
    фио_горничной = Column(ForeignKey("Сотрудники.id"))
    отель = Column(ForeignKey("Отели.id"))
    номер_к_уборке = Column(ForeignKey(Номера.id))
    статус = Column(String)

    def tuple(self):
        return (self.id, self.дата, self.фио_горничной, self.отель, self.номер_к_уборке, self.статус)

