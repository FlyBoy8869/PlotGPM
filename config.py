import configparser
import os

app_root: str = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(app_root, "config.ini")

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

config.add_section("appInfo")
config["appInfo"]["appRoot"] = app_root
config["appInfo"]["appIcon"] = os.path.join(config['appInfo']['appRoot'], "icon.ico")
