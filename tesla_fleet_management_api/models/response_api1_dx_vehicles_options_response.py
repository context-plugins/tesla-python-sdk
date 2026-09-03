from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .vehicle_option import VehicleOption, VehicleOptionDict


class ResponseApi1DxVehiclesOptionsResponse(SdkBaseModel):
    codes: Optional[list[VehicleOption]] = UNSET


class ResponseApi1DxVehiclesOptionsResponseDict(TypedDict):
    codes: NotRequired[list[VehicleOption | VehicleOptionDict]]
