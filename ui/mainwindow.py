from PySide6.QtWidgets import QDialog

from .mainwindow_ui import Ui_MainWindow
from config import config
from plot import plot

VERSION = "0.1.0"

class MainWindowView(QDialog, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle(f"PlotGPM - {VERSION}")
        self.load_default_pressures()
        self.graph_title.setText(config["PLOT"]["title"])

        self.create_graph.clicked.connect(self._create_graph)

    def load_default_pressures(self) -> None:
        pressures = config["PLOT"]["pressures"].split(" ")
        self._set_pressure_label_texts(pressures)

    def _create_graph(self):
        pressures = self._get_pressures()
        flows = self._get_flows()

        if self._validate_flows(flows):
            plot(list(map(int, pressures)), list(map(float,flows)), self.graph_title.text(), self.uut_legend_entry.text())

    def _get_flows(self) -> list[str]:
        return self._get_label_texts("flow")

    def _get_pressures(self) -> list[str]:
        return self._get_label_texts("psi")

    def _get_label_texts(self, prefix) -> list[str]:
        return [getattr(self, f"{prefix}_{index}").text() for index in range(1, 8)]

    def _set_pressure_label_texts(self, pressures) -> None:
        for i in range(1, 8):
            getattr(self, f"{'psi'}_{i}").setText(pressures[i - 1])

    @staticmethod
    def _validate_flows(flows):
        return all(flows)
