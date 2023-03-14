from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt,QSize,  pyqtBoundSignal
from typing import cast
from some_kind_window import set_up_window



class RightUnderWindow(QWidget):


    def __init__(self, parent=None):
        super().__init__(parent)
        self.list_widget = QListWidget()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.list_widget)

        for i in range(10):
            self.add_clickable_widget(f'Action {i}', i)
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
        x = item.data(1000)
        self.help_window = set_up_window(x)
        self.help_window.sh.show()