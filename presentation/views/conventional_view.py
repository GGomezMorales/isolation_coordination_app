from flet import Column, TextField, ElevatedButton, Container, Text, Icons, MainAxisAlignment, CrossAxisAlignment, \
    FontWeight

from core.navigation import Navigator
from presentation.view_models.conventional_vm import ConventionalViewModel


class ConventionalView(Column):
    def __init__(self, navigator: Navigator):
        super().__init__()
        self.navigator: Navigator = navigator
        self.vm: ConventionalViewModel = ConventionalViewModel()

        self.voltage_field = TextField(
            label="Tensión (kV)",
            on_change=self.update_voltage,
            width=300
        )

        self.safety_factor_field = TextField(
            label="Factor de seguridad",
            value=str(self.vm.input_data.safety_factor),
            on_change=self.update_safety_factor,
            width=300
        )

        self.calculate_button = ElevatedButton(
            "Calcular",
            on_click=self.calculate,
            icon=Icons.CALCULATE
        )

        self.result_display = Column()

        self.controls = [
            Container(padding=20),
            self.voltage_field,
            self.safety_factor_field,
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

    def update_safety_factor(self, e):
        self.vm.update_safety_factor(e.control.value)

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
