from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Location1(SdkBaseModel):
    lat: Optional[float] = UNSET
    long: Optional[float] = UNSET


class Location1Dict(TypedDict):
    lat: NotRequired[float]
    long: NotRequired[float]
