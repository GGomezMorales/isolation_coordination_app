from domain.entities import ConventionalInputData, IsolationResult


class ConventionalViewModel:
    def __init__(self):
        self.input_data = ConventionalInputData(
            voltage=0,
            safety_factor=2.0,
            equipment_type="General"
        )
        self.result = None

    def calculate(self):
        # Implementación simplificada del método convencional
        clearance = self.input_data.voltage * 3.0 * self.input_data.safety_factor
        creepage = self.input_data.voltage * 5.0 * self.input_data.safety_factor

        return IsolationResult(
            clearance=round(clearance, 2),
            creepage=round(creepage, 2),
            remarks="Cálculo según método convencional"
        )

    def update_voltage(self, value):
        self.input_data.voltage = float(value)

    def update_safety_factor(self, value):
        self.input_data.safety_factor = float(value)
