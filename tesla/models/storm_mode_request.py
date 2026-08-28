from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class StormModeRequest(SdkBaseModel):
    enabled: bool


class StormModeRequestDict(TypedDict):
    enabled: bool
