import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from random import randint

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.func)
        
        
    def paintEvent(self, e):
        self.paint = QPainter()
        self.paint.begin(self)
        n = randint(25, 250)
        self.paint.drawEllipse(randint(15, 250), randint(15, 250), n, n)
        self.paint.end()

    def func(self):
        self.update()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
