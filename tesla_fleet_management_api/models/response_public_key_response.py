from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ResponsePublicKeyResponse(SdkBaseModel):
    public_key: str


class ResponsePublicKeyResponseDict(TypedDict):
    public_key: str
