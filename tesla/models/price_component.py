from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PriceComponent(SdkBaseModel):
    type_: Optional[str] = Field(default=UNSET, alias="type")
    price: Optional[float] = UNSET
    step_size: Optional[float] = UNSET


class PriceComponentDict(TypedDict):
    type_: NotRequired[str]
    price: NotRequired[float]
    step_size: NotRequired[float]
