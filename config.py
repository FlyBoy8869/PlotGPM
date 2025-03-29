import configparser
import os

app_root = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(app_root, "config.ini")

config = configparser.ConfigParser()
config.read(CONFIG_FILE)
