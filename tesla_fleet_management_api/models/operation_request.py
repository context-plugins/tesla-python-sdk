from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.default_real_mode import DefaultRealModeOrStr


class OperationRequest(SdkBaseModel):
    default_real_mode: DefaultRealModeOrStr


class OperationRequestDict(TypedDict):
    default_real_mode: DefaultRealModeOrStr
