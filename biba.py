from random import randint
from PyQt5.QtCore import Qt,QFile,QIODevice,QTextStream,QTimer
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication,QWidget,QLabel,QVBoxLayout,QPushButton,
    QRadioButton,QHBoxLayout,QMessageBox
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
        self.text = QLabel('Сколько отцов у габена?')
        self.btn1 = QRadioButton('1')
        self.btn2 = QRadioButton('1')
        self.btn3 = QRadioButton('1')
        self.btn4 = QRadioButton('234234234234234456456')
        self.btn1.clicked.connect(self.click)
        self.btn2.clicked.connect(self.click)
        self.btn3.clicked.connect(self.click)
        self.btn4.clicked.connect(self.click)

        vline1 = QVBoxLayout()
        vline1.addWidget(self.btn1)
        vline1.addWidget(self.btn2)

        vline2 = QVBoxLayout()
        vline2.addWidget(self.btn3)
        vline2.addWidget(self.btn4)

        btnLine = QHBoxLayout()
        btnLine.addLayout(vline1)
        btnLine.addLayout(vline2)
        
        mainLine = QVBoxLayout()
        mainLine.addWidget(self.text,alignment=Qt.AlignCenter)
        mainLine.addLayout(btnLine)
        self.setLayout(mainLine)

    def set_styles(self, ui_filename='style.qss', icon='sberbank-pink.jpg'):
        stream = QFile(ui_filename)
        stream.open(QIODevice.ReadOnly)
        self.setStyleSheet(QTextStream(stream).readAll())
        self.setWindowIcon(QtGui.QIcon(icon))

    def message(self,title,txt,w=2000,h=2000 ):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(txt)
        msg.resize(w,h)
        msg.exec_()

    def click(self):
        if self.btn4.isChecked():
            self.message('BepHo!','Не верно! ')
        else:
            self.message('Нет. но..','Да.')

app = QApplication([])
app.setWindowIcon(QtGui.QIcon('sberbank-pink.jpg'))
window = MyWindow('Ета типа кводрот.')
window.show()
app.exec_()
