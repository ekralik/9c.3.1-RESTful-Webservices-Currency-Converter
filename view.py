import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDoubleSpinBox


class MyView(QMainWindow):
     sum: QDoubleSpinBox
     start: QLineEdit
     goal: QLineEdit
     send: QPushButton
     reset: QPushButton
     def __init__(self):
         super().__init__()
         uic.loadUi("gui.ui", self)
         #self.pBGo.clicked.connect(c.submit)
         #self.pBReset.clicked.connect(c.reset)
         #self.reset.clicked.connect(self.reset) # testhalber
         self.reset()

     def setValues(self, sum: float, start: str,goal: str):
        self.sum = sum
        self.start = start
        self.goal = goal
        c = ""
        self.setTxtStatusbar(c)

     def setTxtStatusbar(self, s: str) -> None:
        self.statusbar.showMessage(s)

     def reset(self) -> None:
        self.setValues(10, "EUR", "USD, CHF")

if __name__ == "__main__":
     app = QApplication(sys.argv)
     view = MyView()
     view.show()
     sys.exit(app.exec())