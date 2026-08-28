from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .vehicle_base import VehicleBase, VehicleBaseDict


class Api1VehiclesResponseResponse200(SdkBaseModel):
    response: Optional[VehicleBase] = UNSET


class Api1VehiclesResponseResponse200Dict(TypedDict):
    response: NotRequired[VehicleBase | VehicleBaseDict]
