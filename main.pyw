import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QColor, QPalette
import consts
from create_db import create_db
from login_register import LoginWindow
from mainwindow import MainWindow





if __name__ == "__main__":
    db_is_created = os.path.exists(consts.DATABASE_NAME)
    if not db_is_created:
        create_db()

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

    window = LoginWindow()    # login
    #window = MainWindow()     # not login
    window.show()
    app.exec()


