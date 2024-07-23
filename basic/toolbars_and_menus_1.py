import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        lable = QLabel('Hello!')
        lable.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(lable)

        toolbar = QToolBar('My main toolbar')
        self.addToolBar(toolbar)

    def onMyToolBarButtonClick(self, s):
        print('click', s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
