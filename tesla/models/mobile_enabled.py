from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MobileEnabled(SdkBaseModel):
    result: Optional[bool] = UNSET
    reason: Optional[str] = UNSET


class MobileEnabledDict(TypedDict):
    result: NotRequired[bool]
    reason: NotRequired[str]
