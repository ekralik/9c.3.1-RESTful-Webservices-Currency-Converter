# controller.py

from typing import List
import sys
from PyQt6.QtWidgets import QApplication

import model
import view

class MyController:
    """Controller class for currency conversion application."""
    
    def __init__(self) -> None:
        """Initialize the controller with model and view."""
        self.model = model.CurrencyModel()
        self.view = view.MyView()

        self.view.send.clicked.connect(self.convert)
        self.view.reset.clicked.connect(self.reset)

        self.view.reset_values()
        self.view.show()

    def convert(self) -> None:
        """Convert currency based on user input."""
        try:
            # widgets are still widgets now
            amount = self.view.summ.value()
            source = self.view.start.text().strip().upper()
            targets = [c.strip().upper() for c in self.view.goal.text().split(",") if c.strip()]

            if amount <= 0:
                self.view.setTxtStatusbar("Please enter an amount > 0")
                return
            if not source or not targets:
                self.view.setTxtStatusbar("Please enter source and at least one target currency")
                return

            self.view.setTxtStatusbar("Converting…")

            # Call the model (blocking for now; see non-blocking option below)
            results: List[str] = self.model.convert_currency(amount, source, targets)

            # Format for QTextBrowser; simple and safe
            formatted = "\n".join(results)
            self.view.textBrowser.setPlainText(formatted)

            has_error = any("Fehler" in r or "Error" in r for r in results)
            self.view.setTxtStatusbar("Success" if not has_error else "Check input/API")

        except (ValueError, AttributeError) as e:
            self.view.setTxtStatusbar(f"Error: {str(e)}")

    def submit(self) -> None:
        """Submit default values for testing."""
        default_summ: float = 10.0
        default_source: str = "EUR"
        default_targets: str = "USD, CHF"
        self.view.setValues(
            summ = default_summ,
            start = default_source,
            goal = default_targets
        )

    def reset(self) -> None:
        """Reset the view and model to the initial state."""
        self.view.reset_values()

if __name__ == "__main__":
    """Main entry point of the application."""
    app = QApplication(sys.argv)
    controller = MyController()
    sys.exit(app.exec())