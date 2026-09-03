from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response import Response, ResponseDict


class BackupResponse(SdkBaseModel):
    response: Response


class BackupResponseDict(TypedDict):
    response: Response | ResponseDict
