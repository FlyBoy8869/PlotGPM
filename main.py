import sys

from config import config

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from ui.mainwindow import MainWindowView

APP_ICON_PATH = config['appInfo']['appIcon']

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(APP_ICON_PATH))
    window = MainWindowView()
    window.show()

    sys.exit(app.exec())
