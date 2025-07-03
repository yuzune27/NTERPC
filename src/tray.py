from pystray import Icon, Menu, MenuItem
from PIL import Image
import src.settings as config
from src.path import resource_path

class taskTray:
    def __init__(self):
        self.status = False

        version = config.read_ver()

        # image = Image.open("./img/Icon.png")
        image = Image.open(resource_path("Icon.png"))

        menu = Menu(
            MenuItem(f"Version: {version}", enabled=False, action=None),
            MenuItem("Exit", self.stop_program),
        )

        self.icon = Icon(name="NTERPC", title="NTERPC", icon=image, menu=menu)

    def stop_program(self, icon):
        self.status = False
        icon.stop()

    def run_program(self):
        self.status = True
        self.icon.run()