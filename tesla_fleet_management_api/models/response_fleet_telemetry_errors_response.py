from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .fleet_telemetry_error import FleetTelemetryError, FleetTelemetryErrorDict


class ResponseFleetTelemetryErrorsResponse(SdkBaseModel):
    fleet_telemetry_errors: list[FleetTelemetryError]


class ResponseFleetTelemetryErrorsResponseDict(TypedDict):
    fleet_telemetry_errors: list[FleetTelemetryError | FleetTelemetryErrorDict]
