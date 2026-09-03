from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .charging_period import ChargingPeriod, ChargingPeriodDict
from .location import Location, LocationDict
from .tariffs import Tariffs, TariffsDict
from .total_cost import TotalCost, TotalCostDict


class ChargingSession(SdkBaseModel):
    id: Optional[str] = UNSET
    vin: Optional[str] = UNSET
    model: Optional[str] = UNSET
    start_date_time: Optional[str] = UNSET
    stop_date_time: Optional[str] = UNSET
    total_energy: Optional[float] = UNSET
    total_time: Optional[float] = UNSET
    total_cost: Optional[TotalCost] = UNSET
    location: Optional[Location] = UNSET
    charging_periods: Optional[list[ChargingPeriod]] = UNSET
    tariffs: Optional[Tariffs] = UNSET


class ChargingSessionDict(TypedDict):
    id: NotRequired[str]
    vin: NotRequired[str]
    model: NotRequired[str]
    start_date_time: NotRequired[str]
    stop_date_time: NotRequired[str]
    total_energy: NotRequired[float]
    total_time: NotRequired[float]
    total_cost: NotRequired[TotalCost | TotalCostDict]
    location: NotRequired[Location | LocationDict]
    charging_periods: NotRequired[list[ChargingPeriod | ChargingPeriodDict]]
    tariffs: NotRequired[Tariffs | TariffsDict]
