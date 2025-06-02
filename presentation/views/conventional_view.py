import flet as ft
from presentation.view_models.conventional_vm import ConventionalViewModel


class ConventionalView(ft.Column):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.vm = ConventionalViewModel()

        self.voltage_field = ft.TextField(
            label="Tensión (kV)",
            on_change=self.update_voltage,
            width=300
        )

        self.safety_factor_field = ft.TextField(
            label="Factor de seguridad",
            value=str(self.vm.input_data.safety_factor),
            on_change=self.update_safety_factor,
            width=300
        )

        self.calculate_button = ft.ElevatedButton(
            "Calcular",
            on_click=self.calculate,
            icon=ft.icons.CALCULATE
        )

        self.result_display = ft.Column()

        self.controls = [
            ft.AppBar(title=ft.Text("Método Convencional")),
            ft.Container(padding=20),
            self.voltage_field,
            self.safety_factor_field,
            self.calculate_button,
            ft.Container(padding=10),
            self.result_display,
            ft.ElevatedButton(
                "Volver",
                on_click=self.go_back,
                icon=ft.icons.ARROW_BACK
            )
        ]

        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def update_voltage(self, e):
        self.vm.update_voltage(e.control.value)

    def update_safety_factor(self, e):
        self.vm.update_safety_factor(e.control.value)

    def calculate(self, e):
        result = self.vm.calculate()
        self.result_display.controls = [
            ft.Text(f"Clearance: {result.clearance} mm", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(f"Creepage: {result.creepage} mm", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(result.remarks, size=14)
        ]
        self.update()

    def go_back(self, e):
        self.navigator.go_back()