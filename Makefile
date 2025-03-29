CONFIG_FILE = ./config.ini
INCLUDE_CONFIG = --add-data=$(CONFIG_FILE):.

BASELINE_DATA = ./baseline_flow_data_2008
INCLUDE_BASELINE = --add-data=$(BASELINE_DATA):.

app: clean-all
	uv run pyinstaller --windowed --name PlotGPM $(INCLUDE_CONFIG) $(INCLUDE_BASELINE) main.py

clean-all:
	IF EXIST "build" (rmdir /S /Q build)
	IF EXIST "dist" (rmdir /S /Q dist)
