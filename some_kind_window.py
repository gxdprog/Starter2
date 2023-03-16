from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from myrepo import MyRepository
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QComboBox
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
        s = ["стандарт", "люкс", "апартамент"]
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

a = [ChangeDataHotels, ChangeDataRegions, ChangeDataRooms, ChangeReservRooms, CheckOtchet]
