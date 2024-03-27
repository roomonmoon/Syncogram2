from sql import SQLite
import flet as ft


class Navbar(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.database = SQLite()

        # Labels
        # [from]
        self.navbar_wrapper_from_label = ft.Text()
        self.navbar_wrapper_from_label.value = "From:"
        self.navbar_wrapper_from_label.size = 11
        self.navbar_wrapper_from_label.opacity = 0.5
        # [where]
        self.navbar_wrapper_where_label = ft.Text()
        self.navbar_wrapper_where_label.value = "Where:"
        self.navbar_wrapper_where_label.size = 11
        self.navbar_wrapper_where_label.opacity = 0.5


        # Buttons
        self.add_account_btn = ft.OutlinedButton()
        self.add_account_btn.text = "Add account"
        self.add_account_btn.icon = ft.icons.ADD
        self.add_account_btn.expand = True
        self.add_account_btn.on_click = ...


        self.account_btn = ft.ElevatedButton()
        self.account_btn.text = "Sergey"
        self.account_btn.icon = ft.icons.ACCOUNT_CIRCLE
        self.account_btn.expand = True
        self.account_btn.on_click = ...

        self.settings_btn = ft.ElevatedButton()
        self.settings_btn.text = "Settings"
        self.settings_btn.icon = ft.icons.SETTINGS
        self.settings_btn.expand = True
        self.settings_btn.height = 45


        # Fields
        self.name_field = ft.TextField()
        self.name_field.label = "Name"


        # Divider
        self.navbar_wrapper_divider = ft.Container()
        self.navbar_wrapper_divider.width = 200
        self.navbar_wrapper_divider.height = 0.5
        self.navbar_wrapper_divider.bgcolor = ft.colors.ON_SECONDARY_CONTAINER


        # Containers

        # [ Account controls !NEED TO DYNAMIC GENERATE! ]

        # self.navbar_wrapper_account_container = ft.Column()
        # self.navbar_wrapper_account_container.width = 200
        # self.navbar_wrapper_account_container.controls = [
        #     ft.Row([self.navbar_wrapper_from_label]),
        #     ft.Row([self.navbar_wrapper_divider]),
        #     ft.Row([self.add_account_btn])
        # ]

        # [Major block to display accounts on navbar]
        self.navbar_wrapper_accounts_side = ft.Container()
        self.navbar_wrapper_accounts_side.content = ft.Column([
            self.ui_generate_account_container(True),
            self.ui_generate_account_container(False),
        ])


        # [Settings into bottom menu]
        self.navbar_wrapper_settings = ft.Container(ft.Row([self.settings_btn]))
        self.navbar_wrapper_settings.width = 200
        self.navbar_wrapper_settings.height = 50


        # Main block like canvas to display controls
        self.navbar_wrapper = ft.Container()
        self.navbar_wrapper.content = ft.Column([
            self.navbar_wrapper_accounts_side,
            self.navbar_wrapper_settings,
        ])
        self.navbar_wrapper.content.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.navbar_wrapper.width = 250
        self.navbar_wrapper.padding = 20
        self.navbar_wrapper.content.expand = True
        self.navbar_wrapper.border_radius = ft.BorderRadius(10, 10, 10, 10)
        self.navbar_wrapper.bgcolor = ft.colors.SECONDARY_CONTAINER

    def ui_generate_account_container(self, primary: bool):
        accounts = self.database.get_accounts()

        navbar_wrapper_account_container = ft.Column()
        navbar_wrapper_account_container.width = 200

        if primary:
            navbar_wrapper_account_container.key = "primary"
        else:
            navbar_wrapper_account_container.key = "secondary"

        if not bool(len(accounts)):
            if primary:
                navbar_wrapper_account_container.controls = [
                    ft.Row([self.navbar_wrapper_from_label]),
                    ft.Row([self.navbar_wrapper_divider]),
                    ft.Row([self.add_account_btn])
                ]
            else:
                navbar_wrapper_account_container.controls = [
                    ft.Row([self.navbar_wrapper_where_label]),
                    ft.Row([self.navbar_wrapper_divider]),
                    ft.Row([self.add_account_btn])
                ]

        else:
            for account in accounts:
                if bool(account[2]):
                    navbar_wrapper_account_container.controls.insert(
                        -1, ft.Row([self.add_account_btn])
                    )
                else:
                    ...

        return navbar_wrapper_account_container

    def build(self):
        return self.navbar_wrapper


def application(page: ft.Page):
    # page.theme_mode = ft.ThemeMode.LIGHT
    page.add(
        ft.Row([Navbar(page)], expand=True)
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=application)
