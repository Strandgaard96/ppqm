import configparser
import os
import pathlib
import sys

try:
    pass
except ImportError:
    parent = str(pathlib.Path(__file__).absolute().parent.parent)
    sys.path.insert(0, parent)


def read_settings(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config


SCR = os.environ.get("TMPDIR", "./_tmp_test_")
SCR = pathlib.Path(SCR)
SCR.mkdir(parents=True, exist_ok=True)

# Resources path
RESOURCES = pathlib.Path("tests/resources")

# Try to read config files
configfile = pathlib.Path("development.ini")

if not configfile.is_file():
    configfile = pathlib.Path("production.ini")

if not configfile.is_file():
    configfile = pathlib.Path("default.ini")

CONFIG = read_settings(configfile)
