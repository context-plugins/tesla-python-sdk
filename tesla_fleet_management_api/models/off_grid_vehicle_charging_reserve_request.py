from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OffGridVehicleChargingReserveRequest(SdkBaseModel):
    off_grid_vehicle_charging_reserve_percent: int


class OffGridVehicleChargingReserveRequestDict(TypedDict):
    off_grid_vehicle_charging_reserve_percent: int
