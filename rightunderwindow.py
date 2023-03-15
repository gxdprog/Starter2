from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt,QSize,  pyqtBoundSignal
from typing import cast
from some_kind_window import set_up_window
from create_db import *



class RightUnderWindow(QWidget):

    base: Base

    def __init__(self, base, parent=None):
        super().__init__(parent)
        self.base = base
        self.list_widget = QListWidget()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.list_widget)

        if self.base == Hotels:
            self.add_clickable_widget(f'добавить новый отель')
            self.add_clickable_widget(f'номерной фонд')
            self.add_clickable_widget(f'изменить данные отеля')
        elif self.base == Room:
            self.add_clickable_widget(f'добавить новый номер')
            self.add_clickable_widget(f'изменить данные номера')
        elif self.base == Region:
            self.add_clickable_widget(f'добавить новый регион')
            self.add_clickable_widget(f'изменить данные региона')
        elif self.base == Reservation_log:
            self.add_clickable_widget(f'добавить бронь номера')
            self.add_clickable_widget(f'подтвердить бронь номера')
            self.add_clickable_widget(f'изменить данные брони')
        elif self.base == Guests:
            self.add_clickable_widget(f'добавить нового гостя')
            self.add_clickable_widget(f'изменить данные гостя')
        elif self.base == Clients:
            self.add_clickable_widget(f'добавить нового клиента')
            self.add_clickable_widget(f'изменить данные клиента')
        cast(pyqtBoundSignal, self.list_widget.itemClicked).connect(
            self.handle_itemClicked)

    def add_clickable_widget(self, text):
        item = QListWidgetItem(self.list_widget)
        item.setSizeHint(QSize(0, 40))
        item.setText(text)
        # item.setData(1000, index)
        self.list_widget.addItem(item)

    def handle_itemClicked(self, item: QListWidgetItem):
        if not hasattr(self, "help_window"):
            self.help_window = None
        # x = item.data(1000)
        z = item.text()
        if z == "номерной фонд":
            x = 0
        elif z == 'добавить новый отель':
            x = 1
        elif z == 'добавить новый номер':
            x = 2
        elif z == 'добавить новый регион':
            x = 3
        elif z == 'добавить бронь номера':
            x = 4
        elif z == 'добавить нового гостя':
            x = 5
        elif z == 'подтвердить бронь номера':
            x = 6
        elif z[:8] == 'изменить':
            
        self.help_window = set_up_window(x)
        self.help_window.sh.show()
