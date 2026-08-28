from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response import Response, ResponseDict


class GenericUpdateResponse(SdkBaseModel):
    response: Response


class GenericUpdateResponseDict(TypedDict):
    response: Response | ResponseDict
