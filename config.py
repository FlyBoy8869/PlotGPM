import configparser
import os

app_root = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(app_root, "config.ini")

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

config.add_section("appInfo")
config["appInfo"]["appRoot"] = os.path.dirname(__file__)
config["appInfo"]["appIcon"] = os.path.join(config['appInfo']['appRoot'], "icon.ico")
