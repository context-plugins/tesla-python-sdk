from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .charging_session import ChargingSession, ChargingSessionDict


class ChargingSessionsData(SdkBaseModel):
    data: Optional[list[ChargingSession]] = UNSET
    status_code: Optional[int] = UNSET
    status_message: Optional[str] = UNSET
    timestamp: Optional[dict[str, str]] = UNSET


class ChargingSessionsDataDict(TypedDict):
    data: NotRequired[list[ChargingSession | ChargingSessionDict]]
    status_code: NotRequired[int]
    status_message: NotRequired[str]
    timestamp: NotRequired[dict[str, str]]
