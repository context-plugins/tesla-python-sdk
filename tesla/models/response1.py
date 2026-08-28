from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Response1(SdkBaseModel):
    fleet_telemetry_error_vins: list[str]


class Response1Dict(TypedDict):
    fleet_telemetry_error_vins: list[str]
