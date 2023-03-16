import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QColor, QPalette
import consts
from create_db import *
from myrepo import *
# from login_register import LoginWindow
from mainwindow import MainWindow
from datetime import *





if __name__ == "__main__":
    db_is_created = os.path.exists(consts.DATABASE_NAME)
    if not db_is_created:
        create_db()
        repo = MyRepository()
        repo.add_something(Регионы(название="ЯНАО"))
        repo.add_something(Отели(id=1, название="Небо", регион="ЯНАО", направление="непопулярное", 
                                 начало_мертвого_сезона = date(2023, 12, 1), конец_мертвого_сезона = date(2024, 2, 1)))
        repo.add_something(Отели(id=2, название="Жемчужина", регион="ЯНАО", направление="популярное", 
                                 начало_мертвого_сезона = date(2023, 12, 1), конец_мертвого_сезона = date(2024, 2, 1)))

        repo.add_something(Номера(id=1, номер = 1, отель=1, категория = "стандарт", кол_во_мест=2, статус = "Свободно(чисто)"))
        repo.add_something(Номера(id=2, номер = 2, отель=1, категория = "люкс", кол_во_мест=2, статус = "Свободно(грязно)"))
        repo.add_something(Номера(id=3, номер = 3, отель=1, категория = "апартамент", кол_во_мест=2, статус = "Занято(чисто)"))
        repo.add_something(Номера(id=4, номер = 4, отель=1, категория = "стандарт", кол_во_мест=2, статус = "Занято(грязно)"))

        repo.add_something(Номера(id=5, номер = 1, отель=2, категория = "люкс", кол_во_мест=2, статус = "Свободно(грязно)"))
        repo.add_something(Номера(id=6, номер = 2, отель=2, категория = "апартамент", кол_во_мест=2, статус = "Занято(чисто)"))
        repo.add_something(Номера(id=7, номер = 3, отель=2, категория = "стандарт", кол_во_мест=2, статус = "Занято(грязно)"))
        repo.add_something(Номера(id=8, номер = 4, отель=2, категория = "люкс", кол_во_мест=2, статус = "Свободно(чисто)"))
        repo.add_something(Номера(id=9, номер = 5, отель=2, категория = "стандарт", кол_во_мест=2, статус = "Свободно(чисто)"))


    app = QApplication([])
    app.setStyle("Fusion")
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 220))
    dark_palette.setColor(QPalette.ColorRole.ToolTipText, QColor(1, 1, 1))
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


