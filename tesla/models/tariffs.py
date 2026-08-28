from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .tariff_element import TariffElement, TariffElementDict


class Tariffs(SdkBaseModel):
    currency: Optional[str] = UNSET
    elements: Optional[list[TariffElement]] = UNSET


class TariffsDict(TypedDict):
    currency: NotRequired[str]
    elements: NotRequired[list[TariffElement | TariffElementDict]]
