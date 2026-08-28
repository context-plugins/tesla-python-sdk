from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response_fleet_telemetry_errors_response import (
    ResponseFleetTelemetryErrorsResponse,
    ResponseFleetTelemetryErrorsResponseDict,
)


class FleetTelemetryErrorsResponse(SdkBaseModel):
    response: ResponseFleetTelemetryErrorsResponse


class FleetTelemetryErrorsResponseDict(TypedDict):
    response: ResponseFleetTelemetryErrorsResponse | ResponseFleetTelemetryErrorsResponseDict
