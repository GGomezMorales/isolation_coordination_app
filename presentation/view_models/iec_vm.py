from domain.entities import IECInputData, PollutionLevel
from domain.use_cases.iec_method import IECMethodUseCase


class IECViewModel:
    def __init__(self):
        self.use_case = IECMethodUseCase()
        self.input_data = IECInputData(
            voltage=0,
            pollution_level=PollutionLevel.PL2,
            altitude=0,
            overvoltage_category=2
        )
        self.result = None

    def calculate(self):
        self.result = self.use_case.execute(self.input_data)
        return self.result

    def update_voltage(self, value):
        self.input_data.voltage = float(value)

    def update_pollution_level(self, value):
        self.input_data.pollution_level = PollutionLevel(value)

    def update_altitude(self, value):
        self.input_data.altitude = float(value)

    def update_category(self, value):
        self.input_data.overvoltage_category = int(value)