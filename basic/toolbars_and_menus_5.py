import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        label = QLabel('Hello!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon('bug.png'), 'Your button', self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print('Click', s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
