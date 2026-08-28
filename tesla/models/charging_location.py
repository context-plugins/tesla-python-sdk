from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .location1 import Location1, Location1Dict


class ChargingLocation(SdkBaseModel):
    name: Optional[str] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    distance_miles: Optional[float] = UNSET
    amenities: Optional[str] = UNSET
    available_stalls: Optional[int] = UNSET
    total_stalls: Optional[int] = UNSET
    site_closed: Optional[bool] = UNSET
    billing_info: Optional[str] = UNSET
    location: Optional[Location1] = UNSET


class ChargingLocationDict(TypedDict):
    name: NotRequired[str]
    type_: NotRequired[str]
    distance_miles: NotRequired[float]
    amenities: NotRequired[str]
    available_stalls: NotRequired[int]
    total_stalls: NotRequired[int]
    site_closed: NotRequired[bool]
    billing_info: NotRequired[str]
    location: NotRequired[Location1 | Location1Dict]
