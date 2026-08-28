from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ResponseLiveStatusResponse(SdkBaseModel):
    solar_power: float
    energy_left: float
    total_pack_energy: float
    percentage_charged: float
    backup_capable: bool
    battery_power: Optional[float] = UNSET
    load_power: Optional[float] = UNSET
    grid_status: Optional[str] = UNSET
    grid_power: Optional[float] = UNSET
    island_status: Optional[str] = UNSET
    storm_mode_active: Optional[bool] = UNSET
    timestamp: Optional[RFC3339DateTime] = UNSET


class ResponseLiveStatusResponseDict(TypedDict):
    solar_power: float
    energy_left: float
    total_pack_energy: float
    percentage_charged: float
    backup_capable: bool
    battery_power: NotRequired[float]
    load_power: NotRequired[float]
    grid_status: NotRequired[str]
    grid_power: NotRequired[float]
    island_status: NotRequired[str]
    storm_mode_active: NotRequired[bool]
    timestamp: NotRequired[RFC3339DateTime]
