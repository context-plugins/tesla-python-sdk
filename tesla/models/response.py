from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Response(SdkBaseModel):
    code: int
    message: str


class ResponseDict(TypedDict):
    code: int
    message: str
