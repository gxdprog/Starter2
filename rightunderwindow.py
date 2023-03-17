from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt,QSize,  pyqtBoundSignal
from typing import cast
from some_kind_window import set_up_window
from create_db import *



class RightUnderWindow(QWidget):

    baze = Отели

    def __init__(self, baze, parent=None):
        super().__init__(parent)
        self.baze = baze
        self.list_widget = QListWidget()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.list_widget)

        if self.baze == Отели:
            self.add_clickable_widget(f'Добавить/Изменить отель', 0)
        elif self.baze == Регионы:
            self.add_clickable_widget(f'Добавить регион', 1)
        elif self.baze == Номера:
            self.add_clickable_widget(f'Добавить номер', 2)
            self.add_clickable_widget(f'Добавить бронь номеру', 3)
        elif self.baze == Журнал_бронирования:
            self.add_clickable_widget(f'Создать бронь', 5)
            self.add_clickable_widget(f'Оформить заезд', 8)
            self.add_clickable_widget(f'Оформить выезд', 10)
        elif self.baze == Гости:
            self.add_clickable_widget(f'Добавить гостя', 6)
            self.add_clickable_widget(f'Добавить гостя в группу', 14)
        elif self.baze == Клиенты:
            self.add_clickable_widget(f'Добавить клиента', 7)
        elif self.baze == Списки_гостей:
            self.add_clickable_widget(f'Создать группу гостей', 9)
        elif self.baze == Цены:
            self.add_clickable_widget(f'Добивать/Изменить данные', 11)

        cast(pyqtBoundSignal, self.list_widget.itemClicked).connect(
            self.handle_itemClicked)

    def add_clickable_widget(self, text, index):
        item = QListWidgetItem(self.list_widget)
        item.setSizeHint(QSize(0, 40))
        item.setText(text)
        item.setData(1000, index)
        self.list_widget.addItem(item)

    def handle_itemClicked(self, item: QListWidgetItem):
        if not hasattr(self, "help_window"):
            self.help_window = None
        
        self.help_window = set_up_window(item.data(1000))
        if item.data(1000) != 9:
            self.help_window.sh.show()
