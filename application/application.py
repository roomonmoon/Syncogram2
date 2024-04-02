from configparser import ConfigParser

from sourcefiles import SQLite
from sourcefiles import UserBar
from sourcefiles import MainWindow
from sourcefiles.utils import screensize

import flet as ft

config = ConfigParser()
config.read("config.ini")

__version__ = config.get("Application", "APP_VERSION")

print(__version__)

SCREENWIDTH, SCREENHEIGHT = screensize()

def application(page: ft.Page):
    page.title = config.get("Application", "APP_NAME")
    page.window_width = page.window_min_width = SCREENWIDTH * 0.5
    page.window_height = page.window_min_height = SCREENHEIGHT * 0.7
    page.window_top = SCREENHEIGHT / 8
    page.window_left = (SCREENWIDTH * 0.5) / 2

    page.add(
        ft.Row(
            [
                UserBar(page),
                MainWindow(page),
            ],
            expand=True,
        )
    )

    page.update()


if __name__ == "__main__":
    ft.app(target=application)
