from flet import Column, TextField, Dropdown, ElevatedButton, AppBar, Container, Text, Icons
from flet.core import dropdown
from flet.core.types import MainAxisAlignment, CrossAxisAlignment, FontWeight

from presentation.view_models.iec_vm import IECViewModel


class IECView(Column):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.vm = IECViewModel()

        self.voltage_field = TextField(
            label="Tensión (kV)",
            on_change=self.update_voltage,
            width=300
        )

        self.pollution_dropdown = Dropdown(
            label="Nivel de contaminación",
            options=[dropdown.Option(pl.value) for pl in self.vm.input_data.pollution_level.__class__],
            value=self.vm.input_data.pollution_level.value,
            on_change=self.update_pollution,
            width=300
        )

        self.calculate_button = ElevatedButton(
            "Calcular",
            on_click=self.calculate,
            icon=Icons.CALCULATE
        )

        self.result_display = Column()

        self.controls = [
            AppBar(title=Text("Método IEC 60071-2")),
            Container(padding=20),
            self.voltage_field,
            self.pollution_dropdown,
            self.calculate_button,
            Container(padding=10),
            self.result_display,
            ElevatedButton(
                "Volver",
                on_click=self.go_back,
                icon=Icons.ARROW_BACK
            )
        ]

        self.alignment = MainAxisAlignment.CENTER
        self.horizontal_alignment = CrossAxisAlignment.CENTER

    def update_voltage(self, e):
        self.vm.update_voltage(e.control.value)

    def update_pollution(self, e):
        self.vm.update_pollution_level(e.control.value)

    def calculate(self, e):
        result = self.vm.calculate()
        self.result_display.controls = [
            Text(f"Clearance: {result.clearance} mm", size=18, weight=FontWeight.BOLD),
            Text(f"Creepage: {result.creepage} mm", size=18, weight=FontWeight.BOLD),
            Text(result.remarks, size=14)
        ]
        self.update()

    def go_back(self, e):
        self.navigator.GoBack()
