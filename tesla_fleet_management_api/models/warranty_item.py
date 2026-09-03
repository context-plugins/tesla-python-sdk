from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class WarrantyItem(SdkBaseModel):
    warranty_type: Optional[str] = Field(default=UNSET, alias="warrantyType")
    warranty_display_name: Optional[str] = Field(default=UNSET, alias="warrantyDisplayName")
    expiration_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expirationDate")
    expiration_odometer: Optional[int] = Field(default=UNSET, alias="expirationOdometer")
    odometer_unit: Optional[str] = Field(default=UNSET, alias="odometerUnit")
    warranty_expired_on: OptionalNullable[str] = Field(default=UNSET, alias="warrantyExpiredOn")
    coverage_age_in_years: Optional[int] = Field(default=UNSET, alias="coverageAgeInYears")


class WarrantyItemDict(TypedDict):
    warranty_type: NotRequired[str]
    warranty_display_name: NotRequired[str]
    expiration_date: NotRequired[RFC3339DateTime]
    expiration_odometer: NotRequired[int]
    odometer_unit: NotRequired[str]
    warranty_expired_on: NotRequired[str | None]
    coverage_age_in_years: NotRequired[int]
