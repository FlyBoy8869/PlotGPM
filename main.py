import sys

from PySide6.QtWidgets import QApplication
from ui.mainwindow import MainWindowView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowView()
    window.show()

    sys.exit(app.exec())
