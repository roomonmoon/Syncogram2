import os
import gettext
import flet as ft

from sourcefiles import UserBar
from sourcefiles import MainWindow
from sourcefiles import WelcomeScreenAnimation
from sourcefiles.utils import config
from sourcefiles.utils import newest_version


cfg = config()

script_dir = os.path.dirname(__file__)
pth = os.path.join(script_dir, "locales")

translations = gettext.translation('base', pth, fallback=True)
_ = translations.gettext

async def application(page: ft.Page) -> None:
    page.title = cfg["APP"]["NAME"]
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
    newest_version(page, cfg["APP"]["VERSION"], _)

if __name__ == "__main__":
    ft.app(target=application, assets_dir="assets")
