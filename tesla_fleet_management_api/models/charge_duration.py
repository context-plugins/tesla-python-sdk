from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChargeDuration(SdkBaseModel):
    seconds: int


class ChargeDurationDict(TypedDict):
    seconds: int
