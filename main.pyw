import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QColor, QPalette
import consts
from create_db import *
from myrepo import *
# from login_register import LoginWindow
from mainwindow import MainWindow





if __name__ == "__main__":
    db_is_created = os.path.exists(consts.DATABASE_NAME)
    if not db_is_created:
        create_db()
        mr = MyRepository()
        mr.add_something(Регион(имя="ЯНАО"))
        mr.add_something(Отели(id=1, имя="Отель1", регион="ЯНАО"))
        mr.add_something(Отели(id=2, имя="Отель2", регион="ЯНАО"))
        x = Комната(id=1, отель=1, номер=1, категория="стандарт", места=2, статус="Занят(Чистый)", начало_брони='0000-00-00', конец_брони='0000-00-00')
        mr.add_something(x)
        x = Комната(id=4, отель=2, номер=1, категория="стандарт", места=2, статус="Совбоден(Чистый)", начало_брони='0000-00-00', конец_брони='0000-00-00')
        mr.add_something(x)
        x = Комната(id=5, отель=2, номер=1, категория="стандарт", места=2, статус="Совбоден(Чистый)", начало_брони='0000-00-00', конец_брони='0000-00-00')
        mr.add_something(x)
        x = Комната(id=2, отель=1, номер=2, категория="люкс", места=2, статус="Совбоден(Грязный)", начало_брони='0000-00-00', конец_брони='0000-00-00')
        mr.add_something(x)
        x = Комната(id=3, отель=1, номер=3, категория="апартамент", места=4, статус="Знят(Грязный)", начало_брони='0000-00-00', конец_брони='0000-00-00')
        mr.add_something(x)
        mr.add_something(Клиенты(id = 1, фио = 'namesurpat', тип='fiz'))

    # id = Column(Integer, primary_key=True)
    # hotel = Column(ForeignKey("Hotels.id"))
    # number = Column(String(10))
    # category = Column(String)
    # seats = Column(Integer)
    # status = Column(String)

    app = QApplication([])
    app.setStyle("Fusion")
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 220))
    dark_palette.setColor(QPalette.ColorRole.ToolTipText, QColor(0, 0, 0))
    dark_palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
    dark_palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    app.setPalette(dark_palette)

    #window = LoginWindow()    # login
    window = MainWindow()     # not login
    window.show()
    app.exec()


