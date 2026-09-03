from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .signaling import Signaling, SignalingDict


class Response2(SdkBaseModel):
    signaling: Signaling


class Response2Dict(TypedDict):
    signaling: Signaling | SignalingDict
