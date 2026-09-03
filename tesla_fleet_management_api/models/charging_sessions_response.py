from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .charging_sessions_data import ChargingSessionsData, ChargingSessionsDataDict


class ChargingSessionsResponse(SdkBaseModel):
    response: ChargingSessionsData


class ChargingSessionsResponseDict(TypedDict):
    response: ChargingSessionsData | ChargingSessionsDataDict
