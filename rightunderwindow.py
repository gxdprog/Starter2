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

        if self.base == Отели:
            self.add_clickable_widget(f'добавить новый отель')
            self.add_clickable_widget(f'номерной фонд')
            self.add_clickable_widget(f'изменить данные отеля')
        elif self.base == Комната:
            self.add_clickable_widget(f'добавить новый номер')
            self.add_clickable_widget(f'изменить данные номера')
        elif self.base == Регион:
            self.add_clickable_widget(f'добавить новый регион')
            self.add_clickable_widget(f'изменить данные региона')
        elif self.base == Журнал_бронирования:
            self.add_clickable_widget(f'добавить бронь номера')
            self.add_clickable_widget(f'подтвердить бронь номера')
            self.add_clickable_widget(f'изменить данные брони')
        elif self.base == Гости:
            self.add_clickable_widget(f'добавить нового гостя')
            self.add_clickable_widget(f'изменить данные гостя')
        elif self.base == Клиенты:
            self.add_clickable_widget(f'добавить нового клиента')
            self.add_clickable_widget(f'изменить данные клиента')
        elif self.base == Заезд:
            self.add_clickable_widget(f'оформить новый заезд')
        elif self.base == Группа:
            self.add_clickable_widget(f'создать новую группу')
            self.add_clickable_widget(f'добавить гостя в группу')
            
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
            pass
        elif z == 'оформить новый заезд':
            x = 7
        elif z == 'создать новую группу':
            x = 8
        elif z == 'добавить гостя в группу':
            x = 9
        self.help_window = set_up_window(x)
        if x != 8:
            self.help_window.sh.show()
