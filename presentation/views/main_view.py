from flet import Column, Icons, ElevatedButton, AppBar, Text
from flet.core.types import MainAxisAlignment, CrossAxisAlignment


class MainView(Column):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.controls = [
            AppBar(title=Text("Sistema de Coordinación de Aislamiento")),
            Text("Seleccione método:", size=20),
            ElevatedButton(
                "IEC 60071-2",
                icon=Icons.ELECTRICAL_SERVICES,
                on_click=lambda e: self.navigator.navigate_to('/iec'),
                width=300,
                height=50
            ),
            ElevatedButton(
                "Método Convencional",
                icon=Icons.CALCULATE,
                on_click=lambda e: self.navigator.navigate_to('/conventional'),
                width=300,
                height=50
            )
        ]
        self.alignment = MainAxisAlignment.CENTER
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.spacing = 30
