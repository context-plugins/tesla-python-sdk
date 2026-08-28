from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagination import Pagination, PaginationDict
from .vehicle_base import VehicleBase, VehicleBaseDict


class Api1VehiclesResponse(SdkBaseModel):
    response: Optional[list[VehicleBase]] = UNSET
    pagination: Optional[Pagination] = UNSET
    count: Optional[int] = UNSET


class Api1VehiclesResponseDict(TypedDict):
    response: NotRequired[list[VehicleBase | VehicleBaseDict]]
    pagination: NotRequired[Pagination | PaginationDict]
    count: NotRequired[int]
