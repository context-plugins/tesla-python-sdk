from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response_orders_response import ResponseOrdersResponse, ResponseOrdersResponseDict


class OrdersResponse(SdkBaseModel):
    response: list[ResponseOrdersResponse]
    count: int


class OrdersResponseDict(TypedDict):
    response: list[ResponseOrdersResponse | ResponseOrdersResponseDict]
    count: int
