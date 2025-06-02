from domain.entities import IsolationResult, IECInputData


class IECMethodUseCase:
    def execute(self, data: IECInputData) -> IsolationResult:
        # Implementación del cálculo según IEC 60071-2
        # Ejemplo simplificado:
        base_clearance = data.voltage * 1.5
        base_creepage = data.voltage * 2.5

        # Ajustes por contaminación
        pollution_factors = {
            "PL1": 1.0,
            "PL2": 1.2,
            "PL3": 1.4,
            "PL4": 1.6
        }

        clearance = base_clearance * pollution_factors[data.pollution_level.value]
        creepage = base_creepage * pollution_factors[data.pollution_level.value]

        # Ajuste por altitud
        if data.altitude > 2000:
            clearance *= 1.1
            creepage *= 1.1

        return IsolationResult(
            clearance=round(clearance, 2),
            creepage=round(creepage, 2),
            remarks="Cálculo según IEC 60071-2"
        )
