import gettext
import flet as ft
import os

from sourcefiles import UserBar
from sourcefiles import MainWindow
from sourcefiles import WelcomeScreenAnimation
from sourcefiles.utils import newest_version
from sourcefiles.config import (
    APP_VERSION,
    APP_NAME
)

# file_path = os.path.realpath(__file__)
script_dir = os.path.dirname(__file__)
pth = os.path.join(script_dir, "locales")
path = gettext.find("base", "locales")

with open("/Users/admin/Development/Syncogram/log.txt", "w+", encoding="utf-8") as f:
    f.write(f"Is find locales?: {path}")
    f.write(f"\n")
    f.write(f"Parent dir: {script_dir}")
    f.write(f"\n")
    f.write(f"Full path to locales: {pth}")
    f.write(f"\n")
    f.write(f"Variant 1: {gettext.find("base", "./locales")}")
    f.write(f"\n")
    f.write(f"Variant 2: {gettext.find("base", pth)}")
    f.write(f"\n")
    f.write(f"Variant 3: {gettext.find("base", "../locales")}")
    f.write(f"\n")

translations = gettext.translation('base', pth, fallback=True)
_ = translations.gettext

async def application(page: ft.Page) -> None:
    page.title = APP_NAME
    page.window_width = page.window_min_width = 960
    page.window_height = page.window_min_height = 680
    page.theme_mode = ft.ThemeMode.DARK
    page.window_center()

    mainwindow = MainWindow(page, _)
    userbar = UserBar(page, mainwindow.callback_update, _)
    await WelcomeScreenAnimation(page, _)()

    page.add(
        ft.Row(
            [
                userbar,
                mainwindow,
            ],
            expand=True,
        )
    )
    newest_version(page, APP_VERSION, _)

if __name__ == "__main__":
    ft.app(target=application, assets_dir="assets")
