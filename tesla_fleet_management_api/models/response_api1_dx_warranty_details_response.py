from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .warranty_item import WarrantyItem, WarrantyItemDict


class ResponseApi1DxWarrantyDetailsResponse(SdkBaseModel):
    active_warranty: Optional[list[WarrantyItem]] = Field(default=UNSET, alias="activeWarranty")
    upcoming_warranty: Optional[list[WarrantyItem]] = Field(default=UNSET, alias="upcomingWarranty")
    expired_warranty: Optional[list[WarrantyItem]] = Field(default=UNSET, alias="expiredWarranty")


class ResponseApi1DxWarrantyDetailsResponseDict(TypedDict):
    active_warranty: NotRequired[list[WarrantyItem | WarrantyItemDict]]
    upcoming_warranty: NotRequired[list[WarrantyItem | WarrantyItemDict]]
    expired_warranty: NotRequired[list[WarrantyItem | WarrantyItemDict]]
