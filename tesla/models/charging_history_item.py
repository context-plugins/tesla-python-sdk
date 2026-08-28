from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .charging_fee import ChargingFee, ChargingFeeDict
from .charging_invoice import ChargingInvoice, ChargingInvoiceDict


class ChargingHistoryItem(SdkBaseModel):
    session_id: int = Field(alias="sessionId")
    vin: str
    site_location_name: Optional[str] = Field(default=UNSET, alias="siteLocationName")
    charge_start_date_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="chargeStartDateTime")
    charge_stop_date_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="chargeStopDateTime")
    unlatch_date_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="unlatchDateTime")
    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    fees: Optional[list[ChargingFee]] = UNSET
    billing_type: Optional[str] = Field(default=UNSET, alias="billingType")
    invoices: Optional[list[ChargingInvoice]] = UNSET
    vehicle_make_type: Optional[str] = Field(default=UNSET, alias="vehicleMakeType")


class ChargingHistoryItemDict(TypedDict):
    session_id: int
    vin: str
    site_location_name: NotRequired[str]
    charge_start_date_time: NotRequired[RFC3339DateTime]
    charge_stop_date_time: NotRequired[RFC3339DateTime]
    unlatch_date_time: NotRequired[RFC3339DateTime]
    country_code: NotRequired[str]
    fees: NotRequired[list[ChargingFee | ChargingFeeDict]]
    billing_type: NotRequired[str]
    invoices: NotRequired[list[ChargingInvoice | ChargingInvoiceDict]]
    vehicle_make_type: NotRequired[str]
