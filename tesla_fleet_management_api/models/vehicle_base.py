from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VehicleBase(SdkBaseModel):
    id: Optional[int] = UNSET
    vehicle_id: Optional[int] = UNSET
    vin: Optional[str] = UNSET
    display_name: Optional[str] = UNSET
    access_type: Optional[str] = UNSET
    state: Optional[str] = UNSET
    in_service: Optional[bool] = UNSET
    calendar_enabled: Optional[bool] = UNSET


class VehicleBaseDict(TypedDict):
    id: NotRequired[int]
    vehicle_id: NotRequired[int]
    vin: NotRequired[str]
    display_name: NotRequired[str]
    access_type: NotRequired[str]
    state: NotRequired[str]
    in_service: NotRequired[bool]
    calendar_enabled: NotRequired[bool]
