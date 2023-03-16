from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from myrepo import MyRepository
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QComboBox, QTableWidget, QTableWidgetItem
from create_db import *
from datetime import *


class ChangeDataHotels(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(400, 250)

        self.id_hotel = QLabel("ID отеля:", self)
        self.id_hotel.move(50, 50)

        self.ids_hotel = QComboBox(self)
        self.ids_hotel.move(150, 55)
        mr = MyRepository()
        r = [a.id for a in mr.get_something(Отели)]
        for i in range(1, max(r) + 3):
            if not(i in r):
                m = i
                break
        r.append(m)
        r = set(r)
        r = sorted(r)
        for a in r:
            if a == m:
                self.ids_hotel.addItem(str(a) + "новый")
            else:
                self.ids_hotel.addItem(str(a))
        self.ids_hotel.currentTextChanged.connect(self.fill)


        self.name_hotel = QLabel("Название отеля:", self)
        self.name_hotel.move(50, 90)

        self.input_name_hotel = QLineEdit(self)
        self.input_name_hotel.move(150, 95)
        self.input_name_hotel.resize(200, 20)


        self.reg_hotel = QLabel("Регион отеля:", self)
        self.reg_hotel.move(50, 130)

        self.input_reg_hotel = QComboBox(self)

        mr = MyRepository()
        s = list(mr.get_something(Регионы))
        for a in s:
            self.input_reg_hotel.addItem(str(a.название))
        self.input_reg_hotel.move(150, 130)

        self.submit_button = QPushButton("Подтвердить", self)
        self.submit_button.move(50, 170)
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.resize(200, 40)

        self.fill()

    def fill(self):
        repo = MyRepository()
        r = repo.get_something(Отели)
        flag = 0
        for x in r:
            y = str(x.id)
            if y == self.ids_hotel.currentText():
                r = x
                flag = 1
                break
        if flag:
            self.input_name_hotel.setText(x.название)
            self.input_reg_hotel.setCurrentText(r.регион)
        else:
            self.input_name_hotel.setText('')

    def submit(self):
        id = self.ids_hotel.currentText()
        end = id.find('н')
        if end != -1:
            id = id[:end]
        name = self.input_name_hotel.text()
        reg = self.input_reg_hotel.currentText()
        repo = MyRepository()
        r = repo.get_something(Отели)
        flag = 0
        for x in r:
            y = str(x.id)
            if y == self.ids_hotel.currentText():
                r = x
                flag = 1
                break
        if flag:
            repo.session.delete(r)
            r.название=name
            r.регион = reg
            repo.add_something(r)
        else:
            r = Отели()
            r.id = int(id)
            r.название=name
            r.регион=reg
            repo.add_something(r)
        self.close()


class ChangeDataRegions(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 150)

        self.name_reg = QLabel("Название региона:", self)
        self.name_reg.move(50, 50)
        self.name_reg.resize(200, 20)

        self.input_name_reg = QLineEdit(self)
        self.input_name_reg.move(200, 55)
        self.input_name_reg.resize(200, 20)

        self.submit_button = QPushButton("Подтвердить", self)
        self.submit_button.move(50, 90)
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.resize(200, 40)

    def submit(self):
        repo = MyRepository()
        x = self.input_name_reg.text()
        r = repo.get_something(Регионы)
        flag = 1
        for i in r:
            if i.название == x:
                self.submit_button.setText("Такой регион уже существует")
                flag = 0
        if flag:
            repo.add_something(Регионы(название = x))
        self.close()


class ChangeDataRooms(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 370)

        self.q = QLabel("id номера", self)
        self.q.move(50, 50)
        self.q.resize(200, 20)

        repo = MyRepository()
        r = repo.get_something(Номера)
        r = [int(a.id) for a in r]
        m = 0
        for i in range(1, max(r) + 3):
            if not(i in r):
                m = i
                break

        self.id = QLabel(f"{m}", self)
        self.id.move(200, 55)
        self.id.resize(200, 20)

        self.qqqqqqqqqq = QLabel("Номер номера", self)
        self.qqqqqqqqqq.move(50, 130)
        self.qqqqqqqqqq.resize(200, 20)

        self.number = QLabel("", self)
        self.number.move(200, 130)
        self.number.resize(200, 20)


        self.qq = QLabel("Отель номера", self)
        self.qq.move(50, 90)
        self.qq.resize(200, 20)

        self.hotel = QComboBox(self)
        mr = MyRepository()
        s = list(mr.get_something(Отели))
        for a in s:
            self.hotel.addItem(str(a.id))
        self.hotel.move(200, 90)
        self.hotel.currentTextChanged.connect(self.get_number)


        self.qqq = QLabel("Категория номера:", self)
        self.qqq.move(50, 170)
        self.qqq.resize(200, 20)

        self.category = QComboBox(self)
        mr = MyRepository()
        s = ["стандарт", "люкс", "апартмаент"]
        for a in s:
            self.category.addItem(a)
        self.category.move(200, 175)



        self.qqqq = QLabel("Кол-во мест в номере:", self)
        self.qqqq.move(50, 210)
        self.qqqq.resize(200, 20)

        self.kolvo = QLineEdit(self)
        self.kolvo.move(200, 215)
        self.kolvo.resize(200, 20)



        self.qqqqq = QLabel("Статус номера:", self)
        self.qqqqq.move(50, 250)
        self.qqqqq.resize(200, 20)

        self.status = QComboBox(self)
        mr = MyRepository()
        s = ["Свободно(чисто)", "Свободно(грязно)", "Занято(чисто)", "Занято(грязно)"]
        for a in s:
            self.status.addItem(a)
        self.status.move(200, 255)
        self.status.resize(130, 30)

        self.submit_button = QPushButton("Подтвердить", self)
        self.submit_button.move(50, 290)
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.resize(200, 40)
        self.get_number()

    def get_number(self):
        s = self.hotel.currentText()
        repo = MyRepository()
        r = repo.get_something(Номера)
        rr = []
        for i in r:
            if str(i.отель) == s:
                rr.append(i)
        r = [int(a.номер) for a in rr]
        m = 0
        for i in range(1, max(r) + 3):
            if not(i in r):
                m = i
                break
        self.number.setText(str(m))

    def submit(self):
        repo = MyRepository()
        repo.add_something(Номера(id = self.id.text(), номер = self.number.text(), отель = self.hotel.currentText(), категория = self.category.currentText(),
                                  кол_во_мест=self.kolvo.text(), статус=self.status.currentText()))
        self.close()


class ChangeReservRooms(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 275)

        self.number = QLabel("id номера:", self)
        self.number.move(50, 50)
        self.number.resize(200, 20)

        self.numbers = QComboBox(self)
        mr = MyRepository()
        s = mr.get_something(Номера)
        for a in s:
            self.numbers.addItem(str(a.id))
        self.numbers.move(150, 55)

        self.start = QLabel("Начало брони:", self)
        self.start.move(50, 90)
        self.start.resize(200, 20)

        self.starts = QLineEdit(self)
        self.starts.move(150, 95)
        self.starts.resize(200, 20)
        self.starts.setInputMask("9999-99-99")

        self.end = QLabel("Конец брони:", self)
        self.end.move(50, 130)
        self.end.resize(200, 20)

        self.ends = QLineEdit(self)
        self.ends.move(150, 135)
        self.ends.resize(200, 20)
        self.ends.setInputMask("9999-99-99")

        self.submit_button = QPushButton("Подтвердить", self)
        self.submit_button.move(50, 170)
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.resize(200, 40)

    def submit(self):
        number = self.numbers.currentText()
        mr = MyRepository()
        s = mr.get_something(Номера)
        for a in s:
            if str(a.id) == number:
                r = a
                break
        mr.session.delete(r)
        a = self.starts.text()
        b = self.ends.text()
        try:
            if a < b:
                r.дата_заезда = date(int(a[:a.find('-')]), int(a[a.find('-') + 1: a.rfind('-')]), int(a[a.rfind('-') + 1:]))
                r.дата_выезда = date(int(b[:b.find('-')]), int(b[b.find('-') + 1: b.rfind('-')]), int(b[b.rfind('-') + 1:]))
                mr.add_something(r)
                self.close()
            else:
                self.submit_button.setText("Даты введены неверно")
        except:
            self.submit_button.setText("Даты введены неверно")

class CheckOtchet(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 160)

        self.date = QLabel("Дата отчёта:", self)
        self.date.move(50, 50)
        self.date.resize(200, 20)

        self.dates = QLineEdit(self)
        self.dates.move(150, 55)
        self.dates.resize(200, 20)
        self.dates.setInputMask("9999-99-99")

        self.submit_button = QPushButton("Показать отчёт", self)
        self.submit_button.move(50, 90)
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.resize(200, 40)

    def submit(self):
        a = self.dates.text()
        try:
            d = date(int(a[:a.find('-')]), int(a[a.find('-') + 1: a.rfind('-')]), int(a[a.rfind('-') + 1:]))
            repo = MyRepository()
            r = repo.get_something(Номера)
            ans = []
            for i in r:
                a, b = i.дата_заезда, i.дата_выезда
                if a == None:
                    ans.append([str(i.номер), i.отель])
                elif not(a <= d <= b):
                    ans.append([str(i.номер), i.отель])
            if not hasattr(self, "help_window"):
                self.help_window = None
            self.help_window = Otchet(d, ans)
            self.help_window.show()
            self.close()
        except:
            self.submit_button.setText("Дата введена некорректно")

class Otchet(QMainWindow):
    def __init__(self, date, rooms):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.date = QLabel(f"НА {str(date)} СВОБОДНЫ НОМЕРА", self)
        self.date.move(30, 40)
        self.date.resize(350, 20)
        print(str(date))

        for i in range(len(rooms)):
            self.room = QLabel(f"номер: {rooms[i][0]}   отель: {rooms[i][1]}", self)
            self.room.move(80, 80 + i * 40)
            self.room.resize(200, 20)

        self.setFixedSize(280, 120 + 40 * len(rooms))

class set_up_window:
    sh = None
    def __init__(self, index):
        self.index = index
        self.sh = a[self.index]()


class CreateReserv(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(400, 400)

        self.date = QLabel(f"Дата:", self)
        self.date.move(50, 50)
        self.date.resize(200, 20)
        
        self.dates = QLabel(f"{str(datetime.today())[:10]}", self)
        self.dates.move(150, 50)
        self.dates.resize(200, 20)

        self.zakaz = QLabel(f"Заказчик:", self)
        self.zakaz.move(50, 90)
        self.zakaz.resize(200, 20)

        self.zakazs = QComboBox(self)
        mr = MyRepository()
        s = mr.get_something(Клиенты)
        for a in s:
            self.zakazs.addItem(str(a.id))
        self.zakazs.move(150, 90)

        self.hotel = QLabel(f"Отель:", self)
        self.hotel.move(50, 130)
        self.hotel.resize(200, 20)

        self.hotels = QComboBox(self)
        mr = MyRepository()
        s = mr.get_something(Отели)
        for a in s:
            self.hotels.addItem(str(a.id))
        self.hotels.move(150, 130)
        self.rooms = QComboBox(self)
        self.hotels.currentTextChanged.connect(self.fill_rooms)

        self.room = QLabel(f"Номер:", self)
        self.room.move(50, 170)
        self.room.resize(200, 20)

        mr = MyRepository()
        s = mr.get_something(Номера)
        ans = []
        for a in s:
            if str(a.отель) == self.hotels.currentText() and a.статус in ['Свободно(грязно)', 'Свободно(чисто)']:
                self.rooms.addItem(str(a.id))
        self.rooms.move(150, 170)

        self.check_in = QLabel(f"Дата заезда:", self)
        self.check_in.move(50, 210)
        self.check_in.resize(200, 20)

        self.check_ins = QLineEdit(self)
        self.check_ins.move(150, 210)
        self.check_ins.resize(200, 20)
        self.check_ins.setInputMask("9999-99-99")

        self.check_out = QLabel(f"Дата выезда:", self)
        self.check_out.move(50, 250)
        self.check_out.resize(200, 20)

        self.check_outs = QLineEdit(self)
        self.check_outs.move(150, 250)
        self.check_outs.resize(200, 20)
        self.check_outs.setInputMask("9999-99-99")

        self.price = QLabel(f"Цена:", self)
        self.price.move(50, 290)
        self.price.resize(200, 20)

        self.prices = QLineEdit(self)
        self.prices.move(150, 290)
        self.prices.resize(200, 20)

        self.submit_button = QPushButton("Подтвердить бронирование", self)
        self.submit_button.move(50, 330)
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.resize(200, 40)

    def submit(self):
        a = [self.dates.text(), self.zakazs.currentText(), self.hotels.currentText(), self.rooms.currentText(), self.check_ins.text(),
             self.check_outs.text(), self.prices.text()]
        if not hasattr(self, "help_window"):
            self.x = None
        self.x = ConfirmReserv(a)
        self.x.show()
        self.close()



    def fill_rooms(self):
        self.rooms.clear()
        s = MyRepository().get_something(Номера)
        ans = []
        for a in s:
            if str(a.отель) == self.hotels.currentText() and a.статус in ['Свободно(грязно)', 'Свободно(чисто)']:
                self.rooms.addItem(str(a.id))
        
class ConfirmReserv(QMainWindow):
    def __init__(self, l: list):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(400, 380)

        self.date = QLabel(f"Дата:", self)
        self.date.move(50, 50)
        self.date.resize(200, 20)
        
        self.dates = QLabel(f"{l[0]}", self)
        self.dates.move(150, 50)
        self.dates.resize(200, 20)

        self.zakaz = QLabel(f"Заказчик:", self)
        self.zakaz.move(50, 90)
        self.zakaz.resize(200, 20)

        self.zakazs = QLabel(f"{l[1]}", self)
        self.zakazs.move(150, 90)
        self.zakazs.resize(200, 20)

        self.hotel = QLabel(f"Отель:", self)
        self.hotel.move(50, 130)
        self.hotel.resize(200, 20)

        self.hotels = QLabel(f"{l[2]}", self)
        self.hotels.move(150, 130)
        self.hotels.resize(200, 20)

        self.room = QLabel(f"Номер:", self)
        self.room.move(50, 170)
        self.room.resize(200, 20)

        self.rooms = QLabel(f"{l[3]}", self)
        self.rooms.move(150, 170)
        self.rooms.resize(200, 20)

        self.check_in = QLabel(f"Дата заезда:", self)
        self.check_in.move(50, 210)
        self.check_in.resize(200, 20)

        self.check_ins = QLabel(f"{l[4]}", self)
        self.check_ins.move(150, 210)
        self.check_ins.resize(200, 20)

        self.check_out = QLabel(f"Дата выезда:", self)
        self.check_out.move(50, 250)
        self.check_out.resize(200, 20)

        self.check_outs = QLabel(f"{l[5]}", self)
        self.check_outs.move(150, 250)
        self.check_outs.resize(200, 20)

        self.price = QLabel(f"Цена:", self)
        self.price.move(50, 290)
        self.price.resize(200, 20)

        self.prices = QLineEdit(self)
        self.prices.move(150, 290)
        self.prices.resize(200, 20)
        self.prices.setText(l[6])

        self.submit_button = QPushButton("Подтвердить", self)
        self.submit_button.move(50, 330)
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.resize(200, 40)

    def submit(self):
        repo = MyRepository()
        r = repo.get_something(Журнал_бронирования)
        r = [a.id for a in r]
        r = [0] + r
        for i in range(max(r) + 2):
            if not(i in r):
                m = i
                break
        a = self.check_ins.text()
        d1 = date(int(a[:a.find('-')]), int(a[a.find('-') + 1: a.rfind('-')]), int(a[a.rfind('-') + 1:]))
        a = self.check_outs.text()
        d2 = date(int(a[:a.find('-')]), int(a[a.find('-') + 1: a.rfind('-')]), int(a[a.rfind('-') + 1:]))
        a = self.dates.text()
        d3 = date(int(a[:a.find('-')]), int(a[a.find('-') + 1: a.rfind('-')]), int(a[a.rfind('-') + 1:]))
        if d1 >= d2:
            self.submit_button.setText("неверные даты")
        else:
            x = Журнал_бронирования(отель=self.hotels.text(), заказчик=self.zakazs.text(), id=int(m), номер=self.rooms.text(), 
                                                дата_заезда=d1, дата_выезда=d2, дата = d3)
            repo.add_something(x)
            r = repo.get_something(Номера)
            for i in r:
                if str(i.id) == str(x.номер):
                    z = i
                    break
            repo.session.delete(z)
            r = z
            z = r.статус
            r.статус = 'Занято' + z[z.find('('):]
            r.дата_заезда = d1
            r.дата_выезда = d2
            repo.add_something(r)
            self.close()

class CreateNewGuest(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 200)

        self.number = QLabel("Номер гостя:", self)
        self.number.move(50, 50)
        self.number.resize(200, 20)

        self.numbers = QLineEdit(self)
        self.numbers.move(150, 55)
        self.numbers.resize(200, 20)
        self.numbers.setInputMask('+7(999) 999-99-99')

        self.fio = QLabel("ФИО гостя:", self)
        self.fio.move(50, 90)
        self.fio.resize(200, 20)

        self.fios = QLineEdit(self)
        self.fios.move(150, 90)
        self.fios.resize(200, 20)

        self.submit_button = QPushButton("Подтвердить", self)
        self.submit_button.move(50, 130)
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.resize(200, 40)

    def submit(self):
        repo = MyRepository()
        r = Гости()
        r.телефон = self.numbers.text()
        r.фио = self.fios.text()
        repo.session.add(r)
        repo.session.commit()
        self.close()


class CreateNewClient(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 250)

        self.id = QLabel("id клиента:", self)
        self.id.move(50, 50)
        self.id.resize(200, 20)

        self.ids = QLabel("", self)
        self.ids.move(150, 50)
        self.ids.resize(200, 20)

        repo = MyRepository()
        r = repo.get_something(Клиенты)
        r = [a.id for a in r]
        if len(r):
            for i in range(1, max(r) + 3):
                if not(i in r):
                    r = i
                    break
        else:
            r = 1
        self.ids.setText(f'{r}')

        self.fio = QLabel("Плательщик:", self)
        self.fio.move(50, 90)
        self.fio.resize(200, 20)

        self.fios = QLineEdit(self)
        self.fios.move(150, 90)
        self.fios.resize(200, 20)

        self.type = QLabel(f"Заказчик:", self)
        self.type.move(50, 130)
        self.type.resize(200, 20)

        self.types = QComboBox(self)
        mr = MyRepository()
        s = ["физ. лицо", "юр. лицо"]
        for a in s:
            self.types.addItem(str(a))
        self.types.move(150, 130)

        self.submit_button = QPushButton("Подтвердить", self)
        self.submit_button.move(50, 170)
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.resize(200, 40)

    def submit(self):
        repo = MyRepository()
        r = Клиенты()
        r.id = self.ids.text()
        r.плательщик = self.fios.text()
        r.вид_плательщика = self.types.currentText()
        repo.session.add(r)
        repo.session.commit()
        self.close()    

class CheckIn(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 500)

        self.date = QLabel(f"Дата:", self)
        self.date.move(50, 50)
        self.date.resize(200, 20)
        
        self.dates = QLabel(f"{str(datetime.today())[:10]}", self)
        self.dates.move(150, 50)
        self.dates.resize(200, 20)

        self.bron = QLabel(f"Бронь:", self)
        self.bron.move(50, 90)
        self.bron.resize(200, 20)        
        
        self.brons = QComboBox(self)
        mr = MyRepository()
        s = list(mr.get_something(Журнал_бронирования))
        for a in s:
            self.brons.addItem(str(a.id))
        self.brons.move(150, 90)
        self.brons.currentTextChanged.connect(self.fill_all)        

        self.hotel = QLabel(f"Отель:", self)
        self.hotel.move(50, 130)
        self.hotel.resize(200, 20)        

        self.hotels = QLabel(f"", self)
        self.hotels.move(150, 130)
        self.hotels.resize(200, 20) 

        self.room = QLabel(f"Номер:", self)
        self.room.move(50, 170)
        self.room.resize(200, 20) 

        self.rooms = QLabel(f"", self)
        self.rooms.move(150, 170)
        self.rooms.resize(200, 20) 

        self.in_ = QLabel(f"Дата заезда:", self)
        self.in_.move(50, 210)
        self.in_.resize(200, 20) 

        self.in_s = QLabel(f"", self)
        self.in_s.move(150, 210)
        self.in_s.resize(200, 20) 

        self.out = QLabel(f"Дата выезда:", self)
        self.out.move(50, 250)
        self.out.resize(200, 20) 

        self.outs = QLabel(f"", self)
        self.outs.move(150, 250)
        self.outs.resize(200, 20)

        self.group = QLabel(f"Группа гостей", self)
        self.group.move(50, 290)
        self.group.resize(200, 20)        
        
        self.groups = QComboBox(self)
        mr = MyRepository()
        s = list(mr.get_something(Списки_гостей))
        for a in s:
            self.groups.addItem(str(a.группа))
        self.groups.move(150, 290)

        self.submit_button = QPushButton("Подтвердить", self)
        self.submit_button.move(50, 330)
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.resize(200, 40)

        self.fill_all()

    def fill_all(self):
        repo = MyRepository()
        r = repo.get_something(Журнал_бронирования)
        for i in r:
            if str(i.id) == self.brons.currentText():
                z = i
                break
        self.hotels.setText(str(z.отель))
        self.rooms.setText(str(z.номер))
        self.outs.setText(str(z.дата_выезда))
        self.in_s.setText(str(z.дата_заезда))

    def submit(self):
        repo = MyRepository()
        r = repo.get_something(Номера)
        for i in r:
            if str(i.id) == str(self.rooms.text()):
                z = i
                break
        repo.session.delete(z)
        z.группа_гостей = self.groups.currentText()
        repo.add_something(z)


class CheckOut(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 500)

        self.date = QLabel(f"Дата:", self)
        self.date.move(50, 50)
        self.date.resize(200, 20)
        
        self.dates = QLabel(f"{str(datetime.today())[:10]}", self)
        self.dates.move(150, 50)
        self.dates.resize(200, 20)

        self.bron = QLabel(f"Бронь:", self)
        self.bron.move(50, 90)
        self.bron.resize(200, 20)        
        
        self.brons = QComboBox(self)
        mr = MyRepository()
        s = list(mr.get_something(Журнал_бронирования))
        for a in s:
            self.brons.addItem(str(a.id))
        self.brons.move(150, 90)
        self.brons.currentTextChanged.connect(self.fill_all)        

        self.hotel = QLabel(f"Отель:", self)
        self.hotel.move(50, 130)
        self.hotel.resize(200, 20)        

        self.hotels = QLabel(f"", self)
        self.hotels.move(150, 130)
        self.hotels.resize(200, 20) 

        self.room = QLabel(f"Номер:", self)
        self.room.move(50, 170)
        self.room.resize(200, 20) 

        self.rooms = QLabel(f"", self)
        self.rooms.move(150, 170)
        self.rooms.resize(200, 20) 

        self.in_ = QLabel(f"Дата заезда:", self)
        self.in_.move(50, 210)
        self.in_.resize(200, 20) 

        self.in_s = QLabel(f"", self)
        self.in_s.move(150, 210)
        self.in_s.resize(200, 20) 

        self.out = QLabel(f"Дата выезда:", self)
        self.out.move(50, 250)
        self.out.resize(200, 20) 

        self.outs = QLabel(f"", self)
        self.outs.move(150, 250)
        self.outs.resize(200, 20)

        self.group = QLabel(f"Группа гостей", self)
        self.group.move(50, 290)
        self.group.resize(200, 20)        
        
        self.groups = QLabel(f"", self)
        self.groups.move(150, 290)
        self.groups.resize(200, 20) 

        self.submit_button = QPushButton("Подтвердить", self)
        self.submit_button.move(50, 330)
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.resize(200, 40)

        self.fill_all()

    def fill_all(self):
        repo = MyRepository()
        r = repo.get_something(Журнал_бронирования)
        for i in r:
            if str(i.id) == self.brons.currentText():
                z = i
                break
        self.dates.setText(str(z.дата_выезда))
        r = repo.get_something(Номера)
        for i in r:
            if str(i.id) == str(z.номер):
                self.groups.setText(str(i.группа_гостей))
        self.hotels.setText(str(z.отель))
        self.rooms.setText(str(z.номер))
        self.outs.setText(str(z.дата_выезда))
        self.in_s.setText(str(z.дата_заезда))

    def submit(self):
        repo = MyRepository()
        r = repo.get_something(Номера)
        for i in r:
            if str(i.id) == str(self.rooms.text()):
                z = i
                break
        repo.session.delete(z)
        z.группа_гостей = 'None'
        z.статус = 'Свободный(грязный)'
        z.дата_заезда = None
        z.дата_выезда = None
        repo.add_something(z)
        self.close()



class ChangePrices(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 265)

        self.id = QLabel("id ценника:", self)
        self.id.move(50, 50)
        self.id.resize(200, 20)        
        
        self.ids = QComboBox(self)
        mr = MyRepository()
        s = list(mr.get_something(Цены))
        m = 0
        for a in s:
            self.ids.addItem(str(a.id))
            z = a
            m = z.id
        self.ids.addItem(str(m+1) + " новый")
        self.ids.move(150, 50)
        self.ids.currentTextChanged.connect(self.fill_all)

        self.hotel = QLabel("Отель:", self)
        self.hotel.move(50, 90)
        self.hotel.resize(200, 20)  

        self.hotels = QComboBox(self)
        mr = MyRepository()
        s = list(mr.get_something(Отели))
        for a in s:
            self.hotels.addItem(str(a.id))
        self.hotels.move(150, 90)

        self.categ = QLabel("Категория:", self)
        self.categ.move(50, 130)
        self.categ.resize(200, 20)  

        self.categs = QComboBox(self)
        mr = MyRepository()
        s = ["стандарт", "люкс", "апартмаент"]
        for a in s:
            self.categs.addItem(str(a))
        self.categs.move(150, 130)

        self.price = QLabel("Цена:", self)
        self.price.move(50, 170)
        self.price.resize(200, 20)  

        self.prices = QLineEdit(self)
        self.prices.move(150, 170)
        self.prices.resize(200, 20)

        self.submit_button = QPushButton("Подтвердить", self)
        self.submit_button.move(50, 210)
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.resize(200, 40)
        self.fill_all()

    def fill_all(self):
        repo = MyRepository()
        r = repo.get_something(Цены)
        flag = False
        for i in r:
            if str(i.id) == self.ids.currentText():
                self.categs.clear()
                self.categs.addItem(i.категория)
                self.hotels.setCurrentText(str(i.отель))
                self.prices.setText(str(i.цена))
                flag = True
                break
        if not(flag):
            self.prices.setText("")
            self.categs.clear()
            s = ["стандарт", "люкс", "апартмаент"]
            for a in s:
                self.categs.addItem(str(a))
        else:
            z = self.categs.currentText()
            self.categs.clear()
            self.categs.addItem(z)
            self.categs.move(150, 130)
            



    def submit(self):
        repo = MyRepository()
        x = self.ids.currentText()
        if 'новый' in x:
            jj = self.prices.text()
            p = jj.find('.')
            if p != -1:
                repo.add_something(Цены(id = x[:x.find(' ')], отель=self.hotels.currentText(), категория=self.categs.currentText(), 
                                        цена= jj[:jj.find('.') + 3]))
            else:
                repo.add_something(Цены(id = x[:x.find(' ')], отель=self.hotels.currentText(), категория=self.categs.currentText(), 
                                        цена= jj))
        else:
            r = repo.get_something(Цены)
            for i in r:
                if str(i.id) == str(x):
                    z = i
                    break
            repo.session.delete(z)
            z.отель = self.hotels.currentText()
            z.категория = self.categs.currentText()
            z.цена = self.prices.text()
        self.close()

class ChartPrices(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(500, 250)

        self.prices = QLabel("Отель", self)
        self.prices.move(50, 50)
        self.prices.resize(200, 20)



        self.de = QLabel("стандарт:", self)
        self.de.move(50, 90)
        self.de.resize(200, 20)
        
        self.lu = QLabel("люкс:", self)
        self.lu.move(50, 130)
        self.lu.resize(200, 20)
        
        self.ap = QLabel("апартмаент:", self)
        self.ap.move(50, 170)
        self.ap.resize(200, 20)
        
        self.des = QLabel("", self)
        self.des.move(150, 90)
        self.des.resize(200, 20)
        
        self.lus = QLabel("", self)
        self.lus.move(150, 130)
        self.lus.resize(200, 20)
        
        self.aps = QLabel("", self)
        self.aps.move(150, 170)
        self.aps.resize(200, 20)

        self.qq = QLabel(f"Дата:  {str(datetime.today())[:10]}", self)
        self.qq.move(50, 210)
        self.qq.resize(200, 20)



        self.ids = QComboBox(self)
        mr = MyRepository()
        s = list(mr.get_something(Отели))
        for a in s:
            self.ids.addItem(str(a.id))
        self.ids.move(150, 50)
        self.ids.currentTextChanged.connect(self.fill_table)
        self.fill_table()

    def fill_table(self):
        repo = MyRepository()
        r = repo.get_something(Цены)
        data = [0] * 3
        for i in r:
            if str(i.отель) == self.ids.currentText():
                if i.категория == "стандарт":
                    data[0] = str(i.цена)
                elif i.категория == "люкс":
                    data[1] = str(i.цена)
                else:
                    data[2] = str(i.цена)
        self.des.setText(data[0])
        self.lus.setText(data[1])
        self.aps.setText(data[2])
        



def CreateNewGroup():
    repo = MyRepository()
    r = repo.get_something(Списки_гостей)
    r = [a.группа for a in r]
    r = [0] + r
    for i in range(1, max(r) + 3):
        if not(i in r):
            m = i
            break
    repo.add_something(Списки_гостей(группа=m))


a = [ChangeDataHotels, ChangeDataRegions, ChangeDataRooms, ChangeReservRooms, CheckOtchet, CreateReserv, CreateNewGuest,
      CreateNewClient, CheckIn, CreateNewGroup, CheckOut, ChangePrices, ChartPrices]
