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
        elif self.base == Room:
            self.add_clickable_widget(f'добавить новвый номер')
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
        elif z == 'добавить новвый номер':
            x = 2
        self.help_window = set_up_window(x)
        self.help_window.sh.show()
