from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FleetTelemetryError(SdkBaseModel):
    name: str
    error: str
    vin: str


class FleetTelemetryErrorDict(TypedDict):
    name: str
    error: str
    vin: str
