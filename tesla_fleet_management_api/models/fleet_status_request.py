from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FleetStatusRequest(SdkBaseModel):
    vins: Optional[list[str]] = UNSET


class FleetStatusRequestDict(TypedDict):
    vins: NotRequired[list[str]]
