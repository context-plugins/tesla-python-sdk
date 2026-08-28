from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response_region_response import ResponseRegionResponse, ResponseRegionResponseDict


class RegionResponse(SdkBaseModel):
    response: ResponseRegionResponse


class RegionResponseDict(TypedDict):
    response: ResponseRegionResponse | ResponseRegionResponseDict
