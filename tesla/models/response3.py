from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .charging_location import ChargingLocation, ChargingLocationDict


class Response3(SdkBaseModel):
    destination_charging: Optional[list[ChargingLocation]] = UNSET
    superchargers: Optional[list[ChargingLocation]] = UNSET
    timestamp: Optional[int] = UNSET


class Response3Dict(TypedDict):
    destination_charging: NotRequired[list[ChargingLocation | ChargingLocationDict]]
    superchargers: NotRequired[list[ChargingLocation | ChargingLocationDict]]
    timestamp: NotRequired[int]
