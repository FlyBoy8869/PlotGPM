CONFIG_FILE = ./config.ini
INCLUDE_CONFIG = --add-data=$(CONFIG_FILE):.

BASELINE_DATA = ./baseline_flow_data_2008
INCLUDE_BASELINE = --add-data=$(BASELINE_DATA):.

APP_ICON = icon.ico
INCLUDE_APP_ICON = --add-data=$(APP_ICON):.

APP_NAME = PlotGPM-gui

app: clean-all
	uv run pyinstaller --windowed --icon $(APP_ICON) --name $(APP_NAME) $(INCLUDE_CONFIG) $(INCLUDE_BASELINE) main.py
	copy .\$(APP_ICON) .\dist\$(APP_NAME)\$(APP_ICON)

clean-all:
	IF EXIST "build" (rmdir /S /Q build)
	IF EXIST "dist" (rmdir /S /Q dist)
