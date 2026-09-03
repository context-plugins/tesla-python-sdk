from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TotalCost(SdkBaseModel):
    excl_vat: Optional[float] = UNSET
    incl_vat: Optional[float] = UNSET
    vat: Optional[float] = UNSET


class TotalCostDict(TypedDict):
    excl_vat: NotRequired[float]
    incl_vat: NotRequired[float]
    vat: NotRequired[float]
