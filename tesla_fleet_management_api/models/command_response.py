from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .command_result import CommandResult, CommandResultDict


class CommandResponse(SdkBaseModel):
    response: Optional[CommandResult] = UNSET


class CommandResponseDict(TypedDict):
    response: NotRequired[CommandResult | CommandResultDict]
