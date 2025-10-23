#import Model
import view
import sys
from PyQt6.QtWidgets import QApplication

class MyController:
     def __init__(self):
         #self.model = Model.Wuerfel()
         self.view = view.MyView(self) # View/Controller
         self.reset()
         self.view.show()

     def submit(self) -> None:
         sum = 10
         start = "EUR"
         goal = "USD, CHF"
         self.view.setValues(sum, start, goal)

     def reset(self) -> None:
         self.view.reset()
         #self.model.reset()

if __name__ == "__main__":
     app = QApplication(sys.argv)
     c = MyController()
     sys.exit(app.exec())