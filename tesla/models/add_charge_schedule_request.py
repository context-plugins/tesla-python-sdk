from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AddChargeScheduleRequest(SdkBaseModel):
    lat: float
    lon: float
    id: int
    days_of_week: Optional[str] = UNSET
    start_enabled: Optional[bool] = UNSET
    start_time: Optional[int] = UNSET
    end_enabled: Optional[bool] = UNSET
    end_time: Optional[int] = UNSET
    one_time: Optional[bool] = UNSET
    enabled: bool


class AddChargeScheduleRequestDict(TypedDict):
    lat: float
    lon: float
    id: int
    days_of_week: NotRequired[str]
    start_enabled: NotRequired[bool]
    start_time: NotRequired[int]
    end_enabled: NotRequired[bool]
    end_time: NotRequired[int]
    one_time: NotRequired[bool]
    enabled: bool
