from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .event import Event, EventDict


class ResponseCalendarHistoryResponse(SdkBaseModel):
    events: list[Event]
    total_events: int


class ResponseCalendarHistoryResponseDict(TypedDict):
    events: list[Event | EventDict]
    total_events: int
