from random import *
import sys
from PyQt5.QtCore import Qt,QFile,QIODevice,QTextStream,QTimer
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication,QWidget,QLabel,QVBoxLayout,QPushButton,
    QRadioButton,QHBoxLayout,QMessageBox,QButtonGroup,QGroupBox
)
from const import *
class MyWindow(QWidget):

    def __init__(self,title,w = 400, h =200):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(w,h)
        self.set_styles()
        self.setUi()

    def setUi(self):
        self.text = QLabel('Сколько отцов у габена?')
        self.btn1 = QRadioButton('1')
        self.btn2 = QRadioButton('1')
        self.btn3 = QRadioButton('1')
        self.btn4 = QRadioButton('234234234234234456456')
        self.btns = [self.btn1,self.btn2,self.btn3,self.btn4]
        self.btns_group = QButtonGroup()
        for btn in self.btns:
            self.btns_group.addButton(btn)

        self.button = QPushButton(TO_RES)
        self.button.clicked.connect(self.click)

        self.isRight = QLabel('Правильно or Неправильно?')
        self.rightAnswer = QLabel('Правильный ответ:')

        vline1 = QVBoxLayout()
        vline1.addWidget(self.btn1)
        vline1.addWidget(self.btn2)

        vline2 = QVBoxLayout()
        vline2.addWidget(self.btn3)
        vline2.addWidget(self.btn4)

        test_line = QHBoxLayout()
        test_line.addLayout(vline1)
        test_line.addLayout(vline2)
        self.test_group = QGroupBox('Варианты:')
        self.test_group.setLayout(test_line)

        resLine = QVBoxLayout()
        resLine.addWidget(self.isRight)
        resLine.addWidget(self.rightAnswer,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
        self.resGroup = QGroupBox('Results:')
        self.resGroup.setLayout(resLine)
        self.resGroup.hide()
        self.setQuestion(QS[0])
        
        
        mainLine = QVBoxLayout()
        mainLine.addWidget(self.text,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
        mainLine.addWidget(self.test_group,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
        mainLine.addWidget(self.resGroup,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
        mainLine.setSpacing(3)
        mainLine.addWidget(self.button,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
        self.setLayout(mainLine)

    def toResult(self):
        self.test_group.hide()
        self.resGroup.show()
        self.button.setText(TO_TEST)

    def to_test(self):
        self.btns_group.setExclusive(False)
        for btn in self.btns:
            btn.setChecked(False)
        self.btns_group.setExclusive(True)
        self.test_group.show()
        self.resGroup.hide()
        self.button.setText(TO_RES)


    def setQuestion(self,q):
        shuffle(self.btns)
        self.btns[0].setText(q[RIGHT])
        self.btns[1].setText(q[WRONG][0])
        self.btns[3].setText(q[WRONG][2])
        self.btns[2].setText(q[WRONG][1])
        self.text.setText(q[TEXT])
        self.to_test()


    def click(self):
        if self.button.text() == TO_TEST:
            self.to_test()
        else:
            self.toResult() 

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


app = QApplication([])
app.setWindowIcon(QtGui.QIcon('sberbank-pink.jpg'))
window = MyWindow('Ета типа кводрот.')
window.show()
sys.exit(app.exec_())
