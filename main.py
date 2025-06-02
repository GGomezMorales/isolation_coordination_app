from flet import app, Page, ThemeMode
from flet.core import padding

from core.app import IsolationApp


def main(page: Page) -> None:
    page.title = "Isolation Coordination Method"
    page.padding = padding.all(20)
    page.theme_mode = ThemeMode.LIGHT
    page.window.height = 800
    page.window.width = 600
    page.window.center()

    iso_app: IsolationApp = IsolationApp(page)
    page.add(iso_app)
    page.update()


if __name__ == "__main__":
    app(target=main)
