from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .charge_duration import ChargeDuration, ChargeDurationDict
from .charge_start_time import ChargeStartTime, ChargeStartTimeDict


class ChargeHistory(SdkBaseModel):
    charge_start_time: ChargeStartTime
    charge_duration: ChargeDuration
    energy_added_wh: int


class ChargeHistoryDict(TypedDict):
    charge_start_time: ChargeStartTime | ChargeStartTimeDict
    charge_duration: ChargeDuration | ChargeDurationDict
    energy_added_wh: int
