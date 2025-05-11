import contextlib
import os.path
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QLineEdit
from icecream import ic

from _version import version
from config import config
from plot import plot
from .mainwindow_ui import Ui_MainWindow

ic.configureOutput(includeContext=True)

APP_ICON_PATH = os.path.join(Path(os.path.dirname(__file__)).parent, "icon.ico")


class MainWindowView(QDialog, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowIcon(QIcon(APP_ICON_PATH))
        self.setWindowTitle(f"PlotGPM - {version}")
        self.load_default_pressures()
        self.graph_title.setText(config["PLOT"]["title"])

        self.create_graph.clicked.connect(self._create_graph)

        for widget in self._get_entry_widgets("psi") + self._get_entry_widgets("flow"):
            widget.textChanged.connect(
                lambda _, w=widget: self._validate_entry(w, float)
            )

        self.flow_1.setFocus()

    def load_default_pressures(self) -> None:
        pressures = config["PLOT"]["pressures"].split(" ")
        self._set_pressure_label_texts(pressures)

    def _create_graph(self):
        p_widgets = self._get_entry_widgets("psi")
        f_widgets = self._get_entry_widgets("flow")

        with contextlib.suppress(ValueError):
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

    def _validate_entry(self, widget, type_):
        try:
            type_(widget.text())
            widget.setStyleSheet(
                f"QLineEdit {{ background: {self.palette().ColorRole.Base} }}"
            )
        except ValueError:
            if widget.text():
                widget.setStyleSheet("QLineEdit { background: red }")
            else:
                widget.setStyleSheet(
                    f"QLineEdit {{ background: {self.palette().ColorRole.Base} }}"
                )
