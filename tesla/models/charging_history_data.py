from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .charging_history_item import ChargingHistoryItem, ChargingHistoryItemDict


class ChargingHistoryData(SdkBaseModel):
    data: list[ChargingHistoryItem]


class ChargingHistoryDataDict(TypedDict):
    data: list[ChargingHistoryItem | ChargingHistoryItemDict]
