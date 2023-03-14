from typing import cast
from PyQt6.QtWidgets import QMainWindow, QListWidget, QListWidgetItem, QWidget, QHBoxLayout, QSplitter
from PyQt6.QtCore import pyqtSignal, pyqtBoundSignal, QSize
from PyQt6.QtWidgets import QWidget
from create_db import *

from rightwindow import RightWindow

class MainWindow(QMainWindow):

    my_signal = pyqtSignal(list)
    bases = [Logins]

    def emit_signal(self, signal: list):
        self.my_signal.emit(signal)

    def __init__(self):
        super().__init__()

        self.list_widget = QListWidget()

        for i in range(len(self.bases)):
            t = str(self.bases[i])
            self.add_clickable_widget(t[t.find('.') + 1:t.rfind("'")], i)

        cast(pyqtBoundSignal, self.list_widget.itemClicked).connect(self.handle_itemClicked)

        self.right_window = RightWindow()

        self.my_signal.connect(self.right_window.caught_a_signal)

        splitter = QSplitter()
        splitter.addWidget(self.list_widget)
        splitter.addWidget(self.right_window)

        layout = QHBoxLayout()
        layout.addWidget(splitter)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def add_clickable_widget(self, text, index):
        item = QListWidgetItem(self.list_widget)
        item.setSizeHint(QSize(0, 40))
        item.setText(text)
        item.setData(1000, index)
        self.list_widget.addItem(item)

    def handle_itemClicked(self, item: QListWidgetItem):
        self.emit_signal([self.bases[item.data(1000)]])
