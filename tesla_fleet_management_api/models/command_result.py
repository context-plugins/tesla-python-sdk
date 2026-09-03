from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CommandResult(SdkBaseModel):
    result: bool
    reason: str


class CommandResultDict(TypedDict):
    result: bool
    reason: str
