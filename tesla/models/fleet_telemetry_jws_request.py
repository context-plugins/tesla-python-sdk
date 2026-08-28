from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FleetTelemetryJwsRequest(SdkBaseModel):
    token: Optional[str] = UNSET
    vins: Optional[list[str]] = UNSET


class FleetTelemetryJwsRequestDict(TypedDict):
    token: NotRequired[str]
    vins: NotRequired[list[str]]
