from dataclasses import dataclass
from enum import Enum


class PollutionLevel(Enum):
    PL1 = "PL1"
    PL2 = "PL2"
    PL3 = "PL3"
    PL4 = "PL4"


@dataclass
class IsolationResult:
    clearance: float
    creepage: float
    remarks: str


@dataclass
class IECInputData:
    voltage: float
    pollution_level: PollutionLevel
    altitude: float
    overvoltage_category: int


@dataclass
class ConventionalInputData:
    voltage: float
    safety_factor: float
    equipment_type: str
