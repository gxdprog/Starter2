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
        mr.add_something(Region(name="ЯНАО"))
        mr.add_something(Hotels(id=1, name="Отель1", region="ЯНАО"))
        x = Room(id=1, hotel=1, number=1, category="стандарт", seats=2, status="Чистый")
        mr.add_something(x)
        x = Room(id=2, hotel=1, number=2, category="люкс", seats=2, status="Чистый")
        mr.add_something(x)
        x = Room(id=3, hotel=1, number=3, category="апартамент", seats=4, status="Чистый")
        mr.add_something(x)

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


