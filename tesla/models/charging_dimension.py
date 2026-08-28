from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ChargingDimension(SdkBaseModel):
    type_: Optional[str] = Field(default=UNSET, alias="type")
    volume: Optional[float] = UNSET


class ChargingDimensionDict(TypedDict):
    type_: NotRequired[str]
    volume: NotRequired[float]
