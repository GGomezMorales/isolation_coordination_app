from flet import Column, Page

from core.navigation import Navigator
from presentation.views.main_view import MainView


class IsolationApp(Column):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.navigator = Navigator(self.page, self)
        self._init_app()

    def _init_app(self):
        self.navigator.register_route('/', MainView(self.navigator))
        self.navigator.navigate_to('/')
