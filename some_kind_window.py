import sys
from PyQt6.QtWidgets import QTableView, QWidget, QVBoxLayout, QSplitter
from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from create_db import *
from myrepo import MyRepository
from rightunderwindow import RightUnderWindow

class RightWindow(QWidget):

    repo: MyRepository
    baze = Отели

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Main Window")
        self.table_view = QTableView(self)
        self.repo = MyRepository()

        self.data = [a.tuple() for a in self.repo.get_something(self.baze)]
        self.columns = self.baze.__table__.columns.keys()
        model = MyTableModel(self.data, self.columns)
        self.table_view.setModel(model)
        self.table_view.move(50, 50)

        self.right_lower_window = RightUnderWindow(self.baze)

        self.splitter = QSplitter()
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.addWidget(self.table_view)
        self.splitter.addWidget(self.right_lower_window)

        layout = QVBoxLayout()
        layout.addWidget(self.splitter)

        self.setLayout(layout)

    def caught_a_signal(self, base: list):
        self.baze = base[0]

        delete_me = self.splitter.widget(1)
        delete_me.hide()
        delete_me.deleteLater()

        self.right_lower_window = RightUnderWindow(self.baze)
        self.splitter.addWidget(self.right_lower_window)

        x = self.repo.get_something(self.baze)
        self.data = []
        for a in x:
            self.data.append(a.tuple())
        self.data = [a.tuple() for a in x]
        self.columns = [x.doc for x in self.baze.__table__.columns]
        self.columns = self.baze.__table__.columns.keys()
        model = MyTableModel(self.data, self.columns)
        self.table_view.setModel(model)


class MyTableModel(QAbstractTableModel):
    def __init__(self, data, columns):
        super().__init__()
        self._data = data
        self.__columns = columns

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self.__columns)

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if type(self._data[index.row()]) == type(tuple()):
                return str(self._data[index.row()][index.column()])
            else:
                return str(self._data[index.row()])
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.__columns[section]
