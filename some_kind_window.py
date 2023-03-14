from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from myrepo import MyRepository


class set_up_window:
    sh = None
    def __init__(self, index):
        self.index = index
        self.sh = a[self.index]()

class SomeWindow(QWidget):
    def __del__(self):
        print("DELETED")
        ...
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Second Window0')
        self.setGeometry(150, 150, 300, 200)

        label = QLabel('Hello, world0!', self)
        label.move(100, 50)

        close_button = QPushButton('Close0', self)
        close_button.setGeometry(100, 100, 100, 50)
        close_button.clicked.connect(self.close)


a = [SomeWindow]*30