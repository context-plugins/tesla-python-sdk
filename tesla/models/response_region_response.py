from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ResponseRegionResponse(SdkBaseModel):
    region: str
    fleet_api_base_url: str


class ResponseRegionResponseDict(TypedDict):
    region: str
    fleet_api_base_url: str
