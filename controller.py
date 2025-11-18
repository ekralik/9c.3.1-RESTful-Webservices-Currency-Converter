# controller.py

import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication

import model
import view

class MyController:
    """Controller class for currency conversion application."""

    def __init__(self) -> None:
        """Initialize the controller with mod and view."""
        self.mod = mod.CurrencyModel()
        self.view = view.MyView()

        self.view.send.clicked.connect(self.convert)
        self.view.reset.clicked.connect(self.reset)

        self.view.reset_values()
        self.view.show()

    def convert(self) -> None:
        """
        Convert currency based on user input.
        """
        self.view.set_statusbar("converted")
        try:
            # widgets are still widgets now
            amount = self.view.summ.value()
            source = self.view.start.text().strip().upper()
            targets = [c.strip().upper() for c in self.view.goal.text().split(",") if c.strip()]

            # call your mod; see mod tweak below
            items = self.mod.convert_currency(amount, source, targets)
            # items should be a list of dicts like:
            # [{"target": "USD", "result": 10.67, "rate": 1.067}, ...]

            today = datetime.now().strftime("%d.%m.%Y")

            parts = [f"<p><b>{amount:.2f} {source}</b> entsprechen:</p>", "<ul>"]
            for it in items:
                if "error" in it:  # mod can pass back error for one target
                    parts.append(f"<li><span style='color:#a00;'>{it['error']}</span></li>")
                else:
                    parts.append(
                        f"<li><b>{it['result']:.2f} {it['target']}</b> "
                        f"(Kurs: {it['rate']})</li>"
                    )
            parts.append("</ul>")
            parts.append(f"<p>Stand: {today}</p>")

            self.view.textBrowser.setHtml("\n".join(parts))

        except (ValueError, AttributeError) as e:
            self.view.set_statusbar(f"Error: {str(e)}")

    def submit(self) -> None:
        """Submit default values for testing."""
        default_summ: float = 10.0
        default_source: str = "EUR"
        default_targets: str = "USD, CHF"
        self.view.set_values(
            summ=default_summ,
            start=default_source,
            goal=default_targets
        )

    def reset(self) -> None:
        """Reset the view and mod to the initial state."""
        self.view.reset_values()


if __name__ == "__main__":
    """Main entry point of the application."""
    app = QApplication(sys.argv)
    controller = MyController()
    sys.exit(app.exec())
