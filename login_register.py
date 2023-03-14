from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog
from mainwindow import MainWindow
from create_db import Logins
from myrepo import MyRepository

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Authorization")

        self.setFixedSize(400, 200)

        self.username_label = QLabel("Username:", self)
        self.username_label.move(50, 50)

        self.username_input = QLineEdit(self)
        self.username_input.move(120, 55)
        self.username_input.resize(200, 20)

        self.password_label = QLabel("Password:", self)
        self.password_label.move(50, 80)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.move(120, 85)
        self.password_input.resize(200, 20)

        self.submit_button = QPushButton("Login", self)
        self.submit_button.move(50, 120)
        self.register_button = QPushButton("Registration", self)
        self.register_button.setGeometry(170, 120, 130, 30)
        self.register_button.clicked.connect(self.show_registration_dialog)

        self.wrong_data = QLabel("", self)
        self.wrong_data.setGeometry(50, 150, 1600, 30)

        self.submit_button.clicked.connect(self.submit)
        #self.all_correct()

    def show_registration_dialog(self):
        registration_dialog = RegistrationDialog()
        registration_dialog.exec()

    def submit(self):
        username = self.username_input.text()
        password = self.password_input.text()
        s = MyRepository().session
        s = list(s.query(Logins).filter(Logins.username == username))
        if len(s):
            z = s[0].password
            if z == password:
                self.all_correct()
            else:
                self.password_input.setText('')
                self.wrong_data.setText('Wrong username or password')
        else:
            self.password_input.setText('')
            self.wrong_data.setText('Wrong username or password')

    def all_correct(self):
        self.w = MainWindow()
        self.w.show()
        self.close()

class RegistrationDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registration")

        self.username_label = QLabel("Username:")
        self.password_label = QLabel("Password:")
        self.confirm_password_label = QLabel("Password confirmation:")
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.confirm_password_input = QLineEdit()
        self.register_button = QPushButton("Register")

        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.wronguser = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)
        layout.addWidget(self.wronguser)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        self.register_button.clicked.connect(self.check_passwords)

    def check_passwords(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        z = MyRepository()
        d = list(z.session.query(Logins).filter(Logins.username == username))
        f1 = password == confirm_password
        f2 = len(d) == 0

        if not(f2):
            self.wronguser.setText('this username is already in use')
        elif not(f1):
            self.wronguser.setText("passwords don't match")
        else:
            x = Logins(username=username, password=password)
            z.add_something(x)
            self.close()