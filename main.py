from flet import app, Page
from flet.core.types import ThemeMode

from core.app import IsolationApp


def main(page: Page):
    page.title = "Coordinación de Aislamiento"
    page.theme_mode = ThemeMode.LIGHT
    page.window.height = 800
    page.window.width = 600
    page.window.center()

    app = IsolationApp(page)
    page.add(app)
    page.update()


if __name__ == "__main__":
    app(target=main)
