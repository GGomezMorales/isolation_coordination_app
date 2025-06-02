from flet import Control, Page


class Navigator:
    def __init__(self, page: Page, container: Control):
        self.page = page
        self.container = container
        self.routes = {}
        self.history = []

    def register_route(self, path, view):
        self.routes[path] = view

    def navigate_to(self, path):
        if path in self.routes:
            view = self.routes[path]
            self.container.controls.clear()
            self.container.controls.append(view)
            self.history.append(path)
            self.page.update()

    def go_back(self):
        if len(self.history) > 1:
            self.history.pop()
            prev_path = self.history[-1]
            self.navigate_to(prev_path)
