import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF
from PyQt6 import uic
import io
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(io.StringIO(open('UI.ui').read()), self)
        self.pushButton.clicked.connect(self.run)
        self.x = 1120
        self.y = 900
        self.reg = 0

    def run(self):
        self.reg = 1
        self.update()

    def paintEvent(self, event):
        if self.reg:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.reg = 0

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = random.randrange(1, self.y // 2)
        qp.drawEllipse(QPointF(random.randrange(0, self.x), random.randrange(0, self.y)), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())