from random import randint
from PyQt5.QtCore import Qt,QFile,QIODevice,QTextStream,QTimer
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication,QWidget,QLabel,QVBoxLayout,QPushButton
)
class MyWindow(QWidget):

    def __init__(self,title,w = 400, h =200):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(w,h)
        self.set_styles()
        self.setUi()

    def setUi(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.click)
        self.text = QLabel('Рандомное число от 0 до 100')
        self.number = QLabel('?')
        self.btn = QPushButton('сгенерировать?')
        self.btn.clicked.connect(self.click)
        self.btn.pressed.connect(self.start)
        self.btn.released.connect(self.stop)

        mainLine = QVBoxLayout()
        mainLine.addWidget(self.text,alignment=Qt.AlignCenter)
        mainLine.addWidget(self.number,alignment=Qt.AlignCenter)
        mainLine.addWidget(self.btn,alignment=Qt.AlignCenter)
        self.setLayout(mainLine)

    def set_styles(self, ui_filename='style.qss', icon='sberbank-pink.jpg'):
        stream = QFile(ui_filename)
        stream.open(QIODevice.ReadOnly)
        self.setStyleSheet(QTextStream(stream).readAll())
        self.setWindowIcon(QtGui.QIcon(icon))

    def start(self):
        self.click()
        self.timer.start(350)
    
    def stop(self):
        self.timer.stop()

    def click(self):
        number = randint(0,100)
        self.number.setText(str(number))

app = QApplication([])
window = MyWindow('Ета типа кводрот.')
window.show()
app.exec_()
