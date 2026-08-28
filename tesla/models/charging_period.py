from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .charging_dimension import ChargingDimension, ChargingDimensionDict


class ChargingPeriod(SdkBaseModel):
    start_date_time: Optional[str] = UNSET
    dimensions: Optional[list[ChargingDimension]] = UNSET


class ChargingPeriodDict(TypedDict):
    start_date_time: NotRequired[str]
    dimensions: NotRequired[list[ChargingDimension | ChargingDimensionDict]]
