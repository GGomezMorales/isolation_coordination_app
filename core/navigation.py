from flet import Control, Page


class Navigator:
    def __init__(self, page: Page, container: Control):
        self.page: Page = page
        self.container: Control = container
        self.routes: dict = {}
        self.history: list = []

    def RegisterRoute(self, path: str, view: Control) -> None:
        self.routes[path] = view

    def NavigateTo(self, path: str) -> None:
        if path in self.routes:
            view: Control = self.routes[path]
            self.container.controls.clear()
            self.container.controls.append(view)
            self.history.append(path)
            self.page.update()

    def GoBack(self):
        if len(self.history) > 1:
            self.history.pop()
            prev_path: str = self.history[-1]
            self.NavigateTo(prev_path)
