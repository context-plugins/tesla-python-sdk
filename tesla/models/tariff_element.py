from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .price_component import PriceComponent, PriceComponentDict


class TariffElement(SdkBaseModel):
    price_components: Optional[list[PriceComponent]] = UNSET
    restrictions: Optional[dict[str, Any]] = UNSET


class TariffElementDict(TypedDict):
    price_components: NotRequired[list[PriceComponent | PriceComponentDict]]
    restrictions: NotRequired[dict[str, Any]]
