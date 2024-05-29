import sys

from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect()
        button.clicked.connect()

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print('Clicked!')