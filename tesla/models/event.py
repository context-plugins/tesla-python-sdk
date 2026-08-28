from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class Event(SdkBaseModel):
    timestamp: RFC3339DateTime
    duration: int


class EventDict(TypedDict):
    timestamp: RFC3339DateTime
    duration: int
