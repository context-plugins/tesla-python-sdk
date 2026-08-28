from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AddPreconditionScheduleRequest(SdkBaseModel):
    lat: float
    lon: float
    id: int
    days_of_week: Optional[str] = UNSET
    precondition_time: Optional[int] = UNSET
    one_time: Optional[bool] = UNSET
    enabled: bool


class AddPreconditionScheduleRequestDict(TypedDict):
    lat: float
    lon: float
    id: int
    days_of_week: NotRequired[str]
    precondition_time: NotRequired[int]
    one_time: NotRequired[bool]
    enabled: bool
