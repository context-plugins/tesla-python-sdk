from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Location(SdkBaseModel):
    country: Optional[str] = UNSET
    name: Optional[str] = UNSET


class LocationDict(TypedDict):
    country: NotRequired[str]
    name: NotRequired[str]
