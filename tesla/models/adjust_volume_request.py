from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AdjustVolumeRequest(SdkBaseModel):
    volume: int


class AdjustVolumeRequestDict(TypedDict):
    volume: int
