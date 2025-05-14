import contextlib
import typing

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QLineEdit

from _version import version
from config import config
from plot import plot
from .mainwindow_ui import Ui_MainWindow

APP_ICON_PATH: str = config['appInfo']['appIcon']


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
                lambda text, w=widget: self._apply_visual_validation_to_entry(text, w, float)
            )

        self.flow_1.setFocus()

    def load_default_pressures(self) -> None:
        pressures = config["PLOT"]["pressures"].split(" ")
        self._set_pressure_label_texts(pressures)

    def _create_graph(self) -> None:
        with contextlib.suppress(ValueError):
            plot(
                [int(widget.text()) for widget in self._get_entry_widgets("psi")],
                [float(widget.text()) for widget in self._get_entry_widgets("flow")],
                self.graph_title.text(),
                self.uut_legend_entry.text(),
            )

    def _get_entry_widgets(self, prefix) -> list[QLineEdit]:
        return [getattr(self, f"{prefix}_{index}") for index in range(1, 8)]

    def _set_pressure_label_texts(self, pressures: list[str]) -> None:
        for i in range(1, 8):
            getattr(self, f"{'psi'}_{i}").setText(pressures[i - 1])

    def _apply_visual_validation_to_entry(self, text: str, widget: QLineEdit, converter: typing.Callable) -> None:
        try:
            converter(text)
            widget.setStyleSheet(
                f"QLineEdit {{ background: {self.palette().ColorRole.Base}; color: {self.palette().ColorRole.Text} }}"
            )
        except ValueError:
            if text:
                widget.setStyleSheet("QLineEdit { background: red; color: white }")
            else:
                widget.setStyleSheet(
                    f"QLineEdit {{ background: {self.palette().ColorRole.Base}; color: {self.palette().ColorRole.Text} }}"
                )
