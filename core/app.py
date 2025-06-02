from flet import Column, Page

from core.navigation import Navigator
from presentation.views.conventional_view import ConventionalView
from presentation.views.iec_view import IECView
from presentation.views.main_view import MainView


class IsolationApp(Column):
    def __init__(self, page: Page) -> None:
        super().__init__()
        self.page: Page = page
        self.navigator: Navigator = Navigator(self.page, self)
        self.InitNavigation()

    def InitNavigation(self):
        self.navigator.RegisterRoute('/main', MainView(self.navigator))
        self.navigator.RegisterRoute('/iec', IECView(self.navigator))
        self.navigator.RegisterRoute('/conventional', ConventionalView(self.navigator))
        self.navigator.NavigateTo('/main')
