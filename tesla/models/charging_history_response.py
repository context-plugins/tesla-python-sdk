from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .charging_history_data import ChargingHistoryData, ChargingHistoryDataDict


class ChargingHistoryResponse(SdkBaseModel):
    response: ChargingHistoryData


class ChargingHistoryResponseDict(TypedDict):
    response: ChargingHistoryData | ChargingHistoryDataDict
