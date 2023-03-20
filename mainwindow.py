from typing import cast
from PyQt6.QtWidgets import QMainWindow, QListWidget, QListWidgetItem, QWidget, QHBoxLayout, QSplitter
from PyQt6.QtCore import pyqtSignal, pyqtBoundSignal, QSize
from PyQt6.QtWidgets import QMainWindow, QListWidget, QListWidgetItem, QWidget, QHBoxLayout, QSplitter, QToolBar
from PyQt6.QtWidgets import QWidget
from create_db import *
from PyQt6.QtGui import QAction, QIcon

from rightwindow import RightWindow
from some_kind_window import set_up_window

class MainWindow(QMainWindow):

    my_signal = pyqtSignal(list)
    bases = [Отели, Регионы, 
             Номера, Гости, 
             Клиенты, Журнал_бронирования,
             Списки_гостей, Цены, 
             Сотрудники, 
             Виды_работ, Работа]

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

        toolbar = QToolBar(self)
        self.addToolBar(toolbar)#
        action = QAction(QIcon("icons/free-icon-online-7253175.png"), "Button", self)
        toolbar.addAction(action)
        action.triggered.connect(self.on_click)

        action2 = QAction(QIcon("icons/free-icon-financial-report-3345269.png"), "Button", self)
        toolbar.addAction(action2)
        action2.triggered.connect(self.on_click2)#

        action3 = QAction(QIcon("icons/free-icon-report-3029337.png"), "Button", self)
        toolbar.addAction(action3)
        action3.triggered.connect(self.on_click3)

        action4 = QAction(QIcon("icons/free-icon-maid-1995461.png"), "Button", self)
        toolbar.addAction(action4)
        action4.triggered.connect(self.on_click4)

    def on_click4(self):
        x = 18
        if not hasattr(self, "help_window"):
            self.help_window = None
        self.help_window = set_up_window(x)
        self.help_window.sh.show()

    def on_click3(self):
        x = 13
        if not hasattr(self, "help_window"):
            self.help_window = None
        self.help_window = set_up_window(x)
        self.help_window.sh.show()

    def on_click(self):
        x = 4
        if not hasattr(self, "help_window"):
            self.help_window = None
        self.help_window = set_up_window(x)
        self.help_window.sh.show()

    def on_click2(self):
        x = 12
        if not hasattr(self, "help_window"):
            self.help_window = None
        self.help_window = set_up_window(x)
        self.help_window.sh.show()

    def add_clickable_widget(self, text, index):
        item = QListWidgetItem(self.list_widget)
        item.setSizeHint(QSize(0, 40))
        item.setText(text)
        item.setData(1000, index)
        self.list_widget.addItem(item)

    def handle_itemClicked(self, item: QListWidgetItem):
        self.emit_signal([self.bases[item.data(1000)]])
