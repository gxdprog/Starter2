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
        self.sh = a[self.index]

class RoomCapacity(QMainWindow):
    def __init__(self, parent):
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
        s = mr.session.query(Room).filter(hotel=hotel_id)
        print(list(s))

class Add_New_Hotel(QMainWindow):

    def __init__(self, papar):
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
        self.nameinp.setEchoMode(QLineEdit.EchoMode.Password)
        self.nameinp.move(140, 95)
        self.nameinp.resize(200, 20)

        self.name = QLabel("Регион:", self)
        self.name.move(50, 130)

        
        self.combo_box = QComboBox(self)
        self.combo_box.move(140, 135)
        mr = MyRepository()
        s = list(mr.get_something(Region))
        for a in s:
            self.combo_box.addItem(str(a.name))

        

        self.submit_button = QPushButton("Добавить", self)
        self.submit_button.move(50, 170)
        self.submit_button.clicked.connect(self.add)
        self.submit_button.resize(200, 40)
    
    def add(self):
        a = [self.inpid.text(), self.nameinp.text(), self.combo_box.currentText()]
        mr = MyRepository()
        mr.add_something(Hotels(id=a[0], name=a[1], region=a[2]))

class Add_New_Room(QMainWindow):
    def __init__(self, parent):
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
        s = list(mr.get_something(Hotels))
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

        self.inpseats = QLineEdit(self)
        self.inpseats.move(200, 210)
        self.inpseats.resize(200, 20)

        
        self.status = QLabel("статус комнаты:", self)
        self.status.move(50, 250)

        self.inpstatus = QLineEdit(self)
        self.inpstatus.move(200, 255)
        self.inpstatus.resize(200, 20)
    
    def show_capacity(self):
        hotel_id = self.hotel_input.text()
        mr = MyRepository()
        s = mr.session.query(Room).filter(hotel=hotel_id)
        print(list(s))

class tgesfegsg(QMainWindow):
    def __init__(self, parent):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(400, 200)

        self.id = QLabel("ID отеля:", self)
        self.id.move(50, 50)

        self.inpid = QLineEdit(self)
        self.inpid.move(140, 55)
        self.inpid.resize(200, 20)

        self.name = QLabel("Название отеля:", self)
        self.name.move(50, 90)

        self.nameinp = QLineEdit(self)
        self.nameinp.setEchoMode(QLineEdit.EchoMode.Password)
        self.nameinp.move(140, 95)
        self.nameinp.resize(200, 20)

        self.name = QLabel("Регион:", self)
        self.name.move(50, 130)

        
        combo_box = QComboBox(self)
        combo_box.move(140, 135)
        mr = MyRepository()
        s = list(mr.get_something(Region))
        for a in s:
            combo_box.addItem(str(a.name))
    
    def show_capacity(self):
        hotel_id = self.hotel_input.text()
        mr = MyRepository()
        s = mr.session.query(Room).filter(hotel=hotel_id)
        print(list(s))


a = [RoomCapacity, Add_New_Hotel, Add_New_Room]
