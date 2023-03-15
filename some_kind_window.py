from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QComboBox
from myrepo import MyRepository
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog
from create_db import *
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import pyqtSignal, pyqtBoundSignal, QSize

class set_up_window:
    sh = None
    def __init__(self, index):
        self.index = index
        self.sh = a[self.index]()

class КомнатаCapacity(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(400, 200)

        self.hotel_label = QLabel("ID отеля:", self)
        self.hotel_label.move(50, 50)

        self.hotel_input = QLineEdit(self)
        self.hotel_input.move(120, 55)
        self.hotel_input.resize(200, 20)

        self.submit_button = QPushButton("Показать номерной фонд", self)
        self.submit_button.move(50, 120)
        self.submit_button.clicked.connect(self.show_capacity)
        self.submit_button.resize(200, 20)
    
    def show_capacity(self):
        hotel_id = self.hotel_input.text()
        mr = MyRepository()
        s = mr.session.query(Комната).filter(отель=hotel_id)
        print(list(s))

class Add_New_Hotel(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(400, 300)

        self.id = QLabel("ID отеля:", self)
        self.id.move(50, 50)

        self.inpid = QLineEdit(self)
        self.inpid.move(140, 55)
        self.inpid.resize(200, 20)

        self.name = QLabel("Название отеля:", self)
        self.name.move(50, 90)

        self.nameinp = QLineEdit(self)
        self.nameinp.move(140, 95)
        self.nameinp.resize(200, 20)

        self.name = QLabel("Регион:", self)
        self.name.move(50, 130)

        
        self.combo_box = QComboBox(self)
        self.combo_box.move(140, 135)
        mr = MyRepository()
        s = list(mr.get_something(Регион))
        for a in s:
            self.combo_box.addItem(str(a.имя))

        

        self.submit_button = QPushButton("Добавить", self)
        self.submit_button.move(50, 170)
        self.submit_button.clicked.connect(self.add)
        self.submit_button.resize(200, 40)
    
    def add(self):
        try:
            a = [self.inpid.text(), self.nameinp.text(), self.combo_box.currentText()]
            if len(a[1]) > 150:
                x = 1/0
            mr = MyRepository()
            mr.add_something(Отели(id=a[0], имя=a[1], регион=a[2]))
            self.close()
        except:
            self.submit_button.setText("введены невыерные данные")

class Add_New_Комната(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 400)

        self.id = QLabel("ID комнаты:", self)
        self.id.move(50, 50)

        self.inpid = QLineEdit(self)
        self.inpid.move(200, 55)
        self.inpid.resize(200, 20)

        self.hotel_id = QLabel("ID отеля:", self)
        self.hotel_id.move(50, 90)   

        self.hotel = QComboBox(self)

        mr = MyRepository()
        s = list(mr.get_something(Отели))
        for a in s:
            self.hotel.addItem(str(a.id))
        self.hotel.move(200, 95)

        self.number = QLabel("номер комнаты:", self)
        self.number.move(50, 130)

        self.inpnumber = QLineEdit(self)
        self.inpnumber.move(200, 135)
        self.inpnumber.resize(200, 20)

        self.category = QLabel("категория комнаты:", self)
        self.category.move(50, 170)

        
        self.categorys = QComboBox(self)

        mr = MyRepository()
        s = ["Стандарт", "Люкс", "Апартамент"]
        for a in s:
            self.categorys.addItem(a)
        self.categorys.move(200, 175)

        self.seats = QLabel("кол-во мест в комнате:", self)
        self.seats.move(50, 210)
        self.seats.resize(200, 40)

        self.inpseats = QLineEdit(self)
        self.inpseats.move(200, 215)
        self.inpseats.resize(200, 20)

        
        self.status = QLabel("статус комнаты:", self)
        self.status.move(50, 250)

        self.statuses = QComboBox(self)

        mr = MyRepository()
        s = ["Занят", "Занят(грязный)", "Свободен(Чистый)", "Свободен(Грязный)"]
        for a in s:
            self.statuses.addItem(a)
        self.statuses.move(200, 250)

        self.submit_button = QPushButton("Добавить", self)
        self.submit_button.move(50, 300)
        self.submit_button.clicked.connect(self.add)
        self.submit_button.resize(200, 40)
    
    def add(self):
        try:
            a = [self.inpid.text(), self.hotel.currentText(), self.inpnumber.text(), self.categorys.currentText(), self.inpseats.text(), self.statuses.currentText()]
            mr = MyRepository()
            mr.add_something(Комната(id=a[0], отель=a[1], номер=a[2], категория=a[3], места=a[4], статус=a[5]))
            self.close()
        except:
            self.submit_button.setText("введены невыерные данные")
    
    def show_capacity(self):
        hotel_id = self.hotel_input.text()
        mr = MyRepository()
        s = mr.session.query(Комната).filter(отель=hotel_id)
        print(list(s))

class Add_New_Регион(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 200)

        self.id = QLabel("Название региона:", self)
        self.id.move(50, 50)

        self.inpid = QLineEdit(self)
        self.inpid.move(200, 55)
        self.inpid.resize(150, 20)

        self.submit_button = QPushButton("Добавить", self)
        self.submit_button.move(50, 100)
        self.submit_button.clicked.connect(self.add)
        self.submit_button.resize(200, 40)
    
    def add(self):
        try:
            a = [self.inpid.text()]
            mr = MyRepository()
            mr.add_something(Регион(имя=a[0]))
            self.close()
        except:
            self.submit_button.setText("введены невыерные данные")


class Busing_Room(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 500)

        self.idop = QLabel("ID брони:", self)
        self.idop.move(50, 50)

        self.idopinp = QLineEdit(self)
        self.idopinp.move(150, 55)
        self.idopinp.resize(150, 20)

        self.date = QLabel("дата:", self)
        self.date.move(50, 90)

        self.dateinp = QLineEdit(self)
        self.dateinp.move(150, 95)
        self.dateinp.resize(150, 20)
        self.dateinp.setInputMask("9999-99-99")

        
        self.client_id = QLabel("ID заказчика:", self)
        self.client_id.move(50, 130)

        self.client_ids = QComboBox(self)

        mr = MyRepository()
        s = list(mr.get_something(Клиенты))
        for a in s:
            self.client_ids.addItem(str(a.id))
        self.client_ids.move(150, 135)

        self.hotel_id = QLabel("ID отеля:", self)
        self.hotel_id.move(50, 170)

        self.hotel_ids = QComboBox(self)

        mr = MyRepository()
        s = list(mr.get_something(Отели))
        for a in s:
            self.hotel_ids.addItem(str(a.id))
        self.hotel_ids.move(150, 175)
        self.hotel_ids.currentTextChanged.connect(self.change_rooms)

        self.id = QLabel("ID комнаты:", self)
        self.id.move(50, 210)

        self.idr = QComboBox(self)

        mr = MyRepository()
        s = list(mr.get_something(Комната))
        for a in s:
            if str(a.отель) == self.hotel_ids.currentText() and str(a.статус) in ['Совбоден(Грязный)',
                                                                                  'Совбоден(Чистый)']:
                self.idr.addItem(str(a.id))
        self.idr.move(150, 215)

        
        self.id = QLabel("начало брони:", self)
        self.id.move(50, 250)

        self.startinp = QLineEdit(self)
        self.startinp.move(150, 255)
        self.startinp.resize(150, 20)
        self.startinp.setInputMask("9999-99-99")

                
        self.id = QLabel("конец брони:", self)
        self.id.move(50, 290)

        self.endinp = QLineEdit(self)
        self.endinp.move(150, 295)
        self.endinp.resize(150, 20)
        self.endinp.setInputMask("9999-99-99")

        self.id = QLabel("стоимость:", self)
        self.id.move(50, 330)

        self.priceinp = QLineEdit(self)
        self.priceinp.move(150, 335)
        self.priceinp.resize(150, 20)

        self.submit_button = QPushButton("Добавить", self)
        self.submit_button.move(50, 370)
        self.submit_button.clicked.connect(self.add)
        self.submit_button.resize(200, 40)

    # id = Column(Integer, primary_key=True)
    # date = Column(Date)
    # client = Column(ForeignKey("Клиенты.id"))
    # hotel = Column(ForeignKey("Отели.id"))
    # Комната = Column(ForeignKey("Комната.id"))
    # start_date = Column(Date)
    # end_date = Column(Date)
    # price = Column(String)


    def change_rooms(self):
        self.idr.clear()
        mr = MyRepository()
        s = list(mr.get_something(Комната))
        for a in s:
            if str(a.отель) == self.hotel_ids.currentText():
                self.idr.addItem(str(a.id))
        self.idr.move(150, 215)
    
    def add(self):
        # try:
        mr = MyRepository()
        u = self.priceinp.text()
        i = int(u)
        u = str(u)
        c = 0
        p = ''
        f = 0
        for i in u:
            if i == '.':
                f = 1
            if f:
                c += 1
            if c == 2:
                break
            p += i
        # r = Журнал_бронирования(id=self.idopinp.text(), дата=self.dateinp.text(), клиент=self.client_ids.currentText(), 
        #                     отель = self.hotel_ids.currentText(), комната=self.idr.currentText(), начало_брони=self.startinp.text(), 
        #                     конец_брони=self.endinp.text(), цена = p)
        a = [self.idopinp.text(), self.dateinp.text(), self.client_ids.currentText(), self.hotel_ids.currentText(), 
             self.idr.currentText(), self.startinp.text(), self.endinp.text(), p]
        r = Журнал_бронирования(id=a[0], дата=a[1], заказчик=a[2], отель=a[3], комната=a[4], начало_брони=a[5], конец_брони=a[6], цена=a[7])
        


        mr.add_something(r)
        mr.session.commit()
        # except:
        #     self.submit_button.setText("введены невыерные данные")
        self.close()

class Add_New_Guest(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 200)

        self.number = QLabel("Номер телефона гостя:", self)
        self.number.move(50, 50)

        self.inpnumber = QLineEdit(self)
        self.inpnumber.move(200, 55)
        self.inpnumber.resize(150, 20)
        self.inpnumber.setInputMask("+7(999)999-99-99")

        self.fio = QLabel("ФИО гостя:", self)
        self.fio.move(50, 90)

        self.fioinp = QLineEdit(self)
        self.fioinp.move(200, 95)
        self.fioinp.resize(150, 20)

        self.submit_button = QPushButton("Добавить", self)
        self.submit_button.move(50, 130)
        self.submit_button.clicked.connect(self.add)
        self.submit_button.resize(200, 40)

    
    def add(self):
        try:
            a = [self.fioinp.text(), self.inpnumber.text()]
            mr = MyRepository()
            mr.add_something(Гости(фио=a[0], телефон=a[1]))
            self.close()
        except:
            self.submit_button.setText("введены невыерные данные")

class Confirm_reserv(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(600, 500)

        self.idop = QLabel("ID брони:", self)
        self.idop.move(50, 50)

        self.bron = QComboBox(self)

        mr = MyRepository()
        s = list(mr.get_something(Журнал_бронирования))
        for a in s:
            self.bron.addItem(str(a.id))
        self.bron.move(150, 50)
        self.bron.currentTextChanged.connect(self.change_all)

        self.q1 = QLabel("дата:", self)
        self.q1.move(50, 90)

        self.q1q = QLabel("", self)
        self.q1q.move(150, 90)

        
        self.q2 = QLabel("ID заказчика:", self)
        self.q2.move(50, 130)        
        
        self.q2q =QLabel("", self)
        self.q2q.move(150, 130)



        self.q3 = QLabel("ID отеля:", self)
        self.q3.move(50, 170)        
        
        self.q3q = QLabel("", self)
        self.q3q.move(150, 170)

        self.q4 = QLabel("ID комнаты:", self)
        self.q4.move(50, 210)        
        
        self.q4q =QLabel("", self)
        self.q4q.move(150, 210)

        
        self.q5 = QLabel("начало брони:", self)
        self.q5.move(50, 250)        

        self.q5 = QLabel("ОСНОВАНИЕ", self)
        self.q5.move(250, 200)     
        
        self.q5q = QLabel("", self)
        self.q5q.move(150, 250)

                
        self.q6 = QLabel("конец брони:", self)
        self.q6.move(50, 290)        
        
        self.q6q = QLabel("", self)
        self.q6q.move(150, 290)


        self.qq = QLabel("сумма:", self)
        self.qq.move(50, 315)       

        self.qqq = QLineEdit(self)
        self.qqq.move(150, 320)

        self.submit_button = QPushButton("Подтвердить", self)
        self.submit_button.move(50, 370)
        self.submit_button.clicked.connect(self.add)
        self.submit_button.resize(200, 40)

        self.change_all()
    def change_all(self):
        mr = MyRepository()
        x = mr.get_something(Журнал_бронирования)
        for i in x:
            if str(i.id) == str(self.bron.currentText()):
                x = i
                break
        self.q1q.setText(str(x.дата))
        self.q2q.setText(str(x.заказчик))
        self.q3q.setText(str(x.отель))
        self.q4q.setText(str(x.комната))
        self.q5q.setText(str(x.начало_брони))
        self.q6q.setText(str(x.конец_брони))
        self.qqq.setText(str(x.цена))
    
    def add(self):
        mr = MyRepository()
        a = [self.q1q.text(), self.q2q.text(), self.q3q.text(), self.q4q.text(), self.q5q.text(), self.q6q.text(), self.qqq.text()]
        t = list(mr.session.query(Журнал_бронирования))
        for i in t:
            if str(i.id) == str(self.bron.currentText()):
                t = i
                break

        r = list(mr.session.query(Комната))
        for i in r:
            n = str(t.комната)
            if n == str(i.id):
                r = i
                break
        mr.session.delete(r)
        r.начало_брони = self.q5q.text()
        r.конец_брони = self.q6q.text()
        mr.session.add(r)

        mr.session.delete(t)
        t.цена = a[6]
        mr.add_something(t)
        mr.session.commit()
        self.close()

class Add_New_Check_In(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 300)

        self.date1 = QLabel("Дата оформления заезда:", self)
        self.date1.move(50, 50)

        self.inpdate1 = QLineEdit(self)
        self.inpdate1.move(200, 55)
        self.inpdate1.resize(150, 20)
        self.inpdate1.setInputMask("9999-99-99")

        self.bron = QLabel("Бронь:", self)
        self.bron.move(50, 90)

        self.bron = QComboBox(self)
        mr = MyRepository()
        s = list(mr.get_something(Журнал_бронирования))
        for a in s:
            self.bron.addItem(str(a.id))
        self.bron.move(200, 90)

        self.gg = QLabel("Группа гостей:", self)
        self.gg.move(50, 130)

        self.ggs = QComboBox(self)
        mr = MyRepository()
        s = list(mr.get_something(Группа))
        for a in s:
            self.ggs.addItem(str(a.id))
        self.ggs.move(200, 130)

        self.submit_button = QPushButton("Добавить", self)
        self.submit_button.move(50, 170)
        self.submit_button.clicked.connect(self.add)
        self.submit_button.resize(200, 40)

    def add(self):
        try:
            x = Заезд()
            x.бронь = self.bron.currentText()
            x.дата = self.inpdate1.text()
            mr = MyRepository()
            z = mr.session.query(Журнал_бронирования)
            for i in z:
                if str(i.id) == str(x.бронь):
                    z = i
                    break
            x.отель = z.отель
            x.номер = z.комната
            x.дата_выезда = z.конец_брони
            x.группа_гостей = self.ggs.currentText()
            h = mr.get_something(Заезд)
            h = [int(i.id) for i in h]
            h.append(0)
            for i in range(max(h)+2):
                if not(i in h):
                    x.id = i
                    break
            x.дата_заезда = z.начало_брони
            n = mr.get_something(Комната)
            for i in n:
                if str(i.id) == str(x.номер):
                    n = i
                    break
            mr.session.delete(n)
            u = n.статус
            j = u.find('(')
            u = 'Занят' + u[j:]
            n.статус = u
            mr.add_something(n)
            mr.add_something(x)
            self.close()


        except:
            self.submit_button.setText("введены невыерные данные")

def Add_New_Group():
    mr = MyRepository()
    x = list(mr.get_something(Группа))
    z = [int(a.id) for a in x]
    z.append(0)
    z = max(z) + 1
    mr = MyRepository()
    mr.add_something(Группа(id=z))

class Add_Guest_To_Group(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 200)

        self.number = QLabel("Группа", self)
        self.number.move(50, 50)

        self.zzz = QComboBox(self)
        mr = MyRepository()
        s = list(mr.get_something(Группа))
        for a in s:
            self.zzz.addItem(str(a.id))
        self.zzz.move(150, 50)

        self.number = QLabel("Гость", self)
        self.number.move(50, 90)

        self.ggs = QComboBox(self)
        mr = MyRepository()
        s = list(mr.get_something(Гости))
        for a in s:
            self.ggs.addItem(str(a.телефон))
        self.ggs.move(150, 95)

        self.submit_button = QPushButton("Добавить", self)
        self.submit_button.move(50, 130)
        self.submit_button.clicked.connect(self.add)
        self.submit_button.resize(200, 40)
    
    def add(self):
        try:
            tel = self.ggs.currentText()
            mr = MyRepository()
            x = mr.get_something(Гости)
            for i in x:
                if i.телефон == tel:
                    x = i
                    break
            mr.session.delete(x)
            x.группа = self.zzz.currentText()
            mr.add_something(x)
            self.close()
        except:
            self.submit_button.setText("введены невыерные данные")

a = [КомнатаCapacity, Add_New_Hotel, Add_New_Комната, Add_New_Регион, Busing_Room, Add_New_Guest, Confirm_reserv, Add_New_Check_In,
     Add_New_Group, Add_Guest_To_Group]
