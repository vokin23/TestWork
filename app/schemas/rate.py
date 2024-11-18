from pydantic import BaseModel
from datetime import date


class RateBase(BaseModel):
    cargo_type: str
    rate: float
    date: date


class RateCreate(RateBase):
    pass


class Rate(RateBase):
    id: int

class CalculateInsuranceSchema(BaseModel):
    cargo_type: str
    declared_value: float
    date: str
