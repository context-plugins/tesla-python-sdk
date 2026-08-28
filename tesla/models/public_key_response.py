from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response_public_key_response import ResponsePublicKeyResponse, ResponsePublicKeyResponseDict


class PublicKeyResponse(SdkBaseModel):
    response: ResponsePublicKeyResponse


class PublicKeyResponseDict(TypedDict):
    response: ResponsePublicKeyResponse | ResponsePublicKeyResponseDict
