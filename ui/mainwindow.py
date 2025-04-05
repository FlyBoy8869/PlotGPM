import os.path
from pathlib import Path

from PySide6.QtWidgets import QDialog, QLineEdit
from PySide6.QtGui import QIcon

from .mainwindow_ui import Ui_MainWindow
from config import config
from plot import plot

VERSION = "0.1.0"
APP_ICON_PATH = os.path.join(Path(os.path.dirname(__file__)).parent, "icon.ico")

class MainWindowView(QDialog, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowIcon(QIcon(APP_ICON_PATH))
        self.setWindowTitle(f"PlotGPM - {VERSION}")
        self.load_default_pressures()
        self.graph_title.setText(config["PLOT"]["title"])

        self.create_graph.clicked.connect(self._create_graph)

    def load_default_pressures(self) -> None:
        pressures = config["PLOT"]["pressures"].split(" ")
        self._set_pressure_label_texts(pressures)

    def _create_graph(self):
        p_widgets = self._get_entry_widgets("psi")
        f_widgets = self._get_entry_widgets("flow")

        if all(widget.hasAcceptableInput() for widget in p_widgets) and all(widget.hasAcceptableInput() for widget in f_widgets):
            plot(
                [int(widget.text()) for widget in p_widgets],
                [float(widget.text()) for widget in f_widgets],
                self.graph_title.text(),
                self.uut_legend_entry.text(),
            )

    def _get_entry_widgets(self, prefix) -> list[QLineEdit]:
        return [getattr(self, f"{prefix}_{index}") for index in range(1, 8)]

    def _set_pressure_label_texts(self, pressures) -> None:
        for i in range(1, 8):
            getattr(self, f"{'psi'}_{i}").setText(pressures[i - 1])
