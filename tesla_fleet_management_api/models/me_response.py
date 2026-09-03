from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response_me_response import ResponseMeResponse, ResponseMeResponseDict


class MeResponse(SdkBaseModel):
    response: ResponseMeResponse


class MeResponseDict(TypedDict):
    response: ResponseMeResponse | ResponseMeResponseDict
