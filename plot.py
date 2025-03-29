import os

from config import config
import json
import matplotlib.pyplot as plt

app_root = os.path.dirname(__file__)
BASELINE_FILE = os.path.join(app_root, "baseline_flow_data_2008")


def config_get(section: str, key: str):
    return config[section][key]


def plot(pressures, flows, title, uut_legend_label):
    with open(BASELINE_FILE, mode="rb") as fp:
        baseline_flow_data = json.load(fp)

    plt.plot(baseline_flow_data["flow data"], pressures, "bD", label=baseline_flow_data["legend key"])
    plt.plot(flows, pressures, "ro", label=uut_legend_label)
    plt.title(title)
    plt.xlabel(config_get("PLOT", "xLabel"))
    plt.ylabel(config_get("PLOT", "yLabel"))
    if config_get("PLOT", "minorTickMarks") == "true":
        plt.minorticks_on()
    plt.grid(True, which="both", axis=config["PLOT"]["axis"], linestyle="--")
    plt.legend()
    plt.show()
