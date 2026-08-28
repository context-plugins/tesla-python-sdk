from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .vehicle_base import VehicleBase, VehicleBaseDict


class Api1VehiclesResponseGetVehicle(SdkBaseModel):
    response: Optional[VehicleBase] = UNSET


class Api1VehiclesResponseGetVehicleDict(TypedDict):
    response: NotRequired[VehicleBase | VehicleBaseDict]
