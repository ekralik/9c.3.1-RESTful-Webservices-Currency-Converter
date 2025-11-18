# view.py

import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDoubleSpinBox, QTextBrowser, \
    QStatusBar

class MyView(QMainWindow):
    summ: QDoubleSpinBox
    start: QLineEdit
    goal: QLineEdit
    send: QPushButton
    reset: QPushButton
    close_button: QPushButton
    textBrowser: QTextBrowser
    statusbar: QStatusBar

    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.setWindowTitle("Currency Converter")
        self.setFixedSize(655, 330)
        self.reset_values()


    def set_values(self, summ: float, start: str, goal: str):
        """

        :param summ:
        :param start:
        :param goal:
        :return:
        """
        self.summ.setValue(summ)
        self.start.setText(start)
        self.goal.setText(goal)
        self.set_statusbar("ready")


    def set_statusbar(self, s: str) -> None:
        """

        :param s:
        :return:
        """
        self.statusbar.showMessage(s)

    def reset_values(self) -> None:
        """

        :return:
        """
        self.set_values(0.0, "", "")
        self.textBrowser.setPlainText("")
        self.summ.setValue(0)

    def standard_values(self) -> None:
        """

        :return:
        """
        self.set_values(10.0, "EUR", "USD, CHF")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MyView()
    view.show()
    sys.exit(app.exec())
