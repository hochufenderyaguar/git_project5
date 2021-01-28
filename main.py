import sys
from PyQt5 import uic
from random import randint, choices
from PyQt5.QtGui import QPainter, QColor, QPen
from ui_file import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        for _ in range(10):
            pen = QPen()
            pen.setColor(QColor(QColor(*choices(range(256), k=3))))
            qp.setPen(pen)
            d = randint(1, min(self.width(), self.height()))
            qp.drawEllipse(randint(0, self.width()), randint(0, self.height()), d, d)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    win = Window()
    win.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
