from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .driver import Driver, DriverDict


class DriversResponse(SdkBaseModel):
    response: Optional[list[Driver]] = UNSET
    count: Optional[int] = UNSET


class DriversResponseDict(TypedDict):
    response: NotRequired[list[Driver | DriverDict]]
    count: NotRequired[int]
