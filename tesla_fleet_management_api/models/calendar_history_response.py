from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response_calendar_history_response import ResponseCalendarHistoryResponse, ResponseCalendarHistoryResponseDict


class CalendarHistoryResponse(SdkBaseModel):
    response: ResponseCalendarHistoryResponse


class CalendarHistoryResponseDict(TypedDict):
    response: ResponseCalendarHistoryResponse | ResponseCalendarHistoryResponseDict
