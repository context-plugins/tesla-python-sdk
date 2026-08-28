from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .mobile_enabled import MobileEnabled, MobileEnabledDict


class Api1VehiclesMobileEnabledResponse(SdkBaseModel):
    response: Optional[MobileEnabled] = UNSET


class Api1VehiclesMobileEnabledResponseDict(TypedDict):
    response: NotRequired[MobileEnabled | MobileEnabledDict]
