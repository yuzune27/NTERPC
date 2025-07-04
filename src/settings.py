import configparser
import json
import os
import sys
from src.PlayerData import PlayerData
from src.path import get_executable_dir


def read_ver():
    config = configparser.ConfigParser()
    if hasattr(sys, '_MEIPASS'):
        version_path = os.path.join(get_executable_dir(), 'settings', 'version.ini')
    else:
        version_path = './settings/version.ini'

    config.read(version_path, encoding="utf-8")
    return config["PROFILE"]["Version"]


def get_userdata():
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    try:
        with open("./settings/config.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        with open(rf"{script_dir}\settings\config.json", "r", encoding="UTF-8") as f:
            data = json.load(f)

    player_data = PlayerData(
        Player=data["Player"],
        UID=data["UID"],
        UIDVisible=data["UIDVisible"],
        BtnLabel = data["BtnLabel"],
        BtnUrl = data["BtnUrl"],
    )

    return player_data
