from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ResponseOrdersResponse(SdkBaseModel):
    vehicle_map_id: int = Field(alias="vehicleMapId")
    reference_number: str = Field(alias="referenceNumber")
    vin: str
    order_status: str = Field(alias="orderStatus")
    order_substatus: str = Field(alias="orderSubstatus")
    model_code: str = Field(alias="modelCode")
    country_code: str = Field(alias="countryCode")
    locale: str
    mkt_options: str = Field(alias="mktOptions")
    is_b2b: bool = Field(alias="isB2b")


class ResponseOrdersResponseDict(TypedDict):
    vehicle_map_id: int
    reference_number: str
    vin: str
    order_status: str
    order_substatus: str
    model_code: str
    country_code: str
    locale: str
    mkt_options: str
    is_b2b: bool
