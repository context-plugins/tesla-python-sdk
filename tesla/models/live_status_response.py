from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response_live_status_response import ResponseLiveStatusResponse, ResponseLiveStatusResponseDict


class LiveStatusResponse(SdkBaseModel):
    response: ResponseLiveStatusResponse


class LiveStatusResponseDict(TypedDict):
    response: ResponseLiveStatusResponse | ResponseLiveStatusResponseDict
