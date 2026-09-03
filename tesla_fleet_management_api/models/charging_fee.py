from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ChargingFee(SdkBaseModel):
    session_fee_id: Optional[int] = Field(default=UNSET, alias="sessionFeeId")
    fee_type: Optional[str] = Field(default=UNSET, alias="feeType")
    currency_code: Optional[str] = Field(default=UNSET, alias="currencyCode")
    pricing_type: Optional[str] = Field(default=UNSET, alias="pricingType")
    rate_base: Optional[float] = Field(default=UNSET, alias="rateBase")
    rate_tier1: Optional[float] = Field(default=UNSET, alias="rateTier1")
    rate_tier2: Optional[float] = Field(default=UNSET, alias="rateTier2")
    rate_tier3: OptionalNullable[float] = Field(default=UNSET, alias="rateTier3")
    rate_tier4: OptionalNullable[float] = Field(default=UNSET, alias="rateTier4")
    usage_base: Optional[float] = Field(default=UNSET, alias="usageBase")
    usage_tier1: Optional[float] = Field(default=UNSET, alias="usageTier1")
    usage_tier2: Optional[float] = Field(default=UNSET, alias="usageTier2")
    usage_tier3: OptionalNullable[float] = Field(default=UNSET, alias="usageTier3")
    usage_tier4: OptionalNullable[float] = Field(default=UNSET, alias="usageTier4")
    total_base: Optional[float] = Field(default=UNSET, alias="totalBase")
    total_tier1: Optional[float] = Field(default=UNSET, alias="totalTier1")
    total_tier2: Optional[float] = Field(default=UNSET, alias="totalTier2")
    total_tier3: Optional[float] = Field(default=UNSET, alias="totalTier3")
    total_tier4: Optional[float] = Field(default=UNSET, alias="totalTier4")
    total_due: Optional[float] = Field(default=UNSET, alias="totalDue")
    net_due: Optional[float] = Field(default=UNSET, alias="netDue")
    uom: Optional[str] = UNSET
    is_paid: Optional[bool] = Field(default=UNSET, alias="isPaid")
    status: Optional[str] = UNSET


class ChargingFeeDict(TypedDict):
    session_fee_id: NotRequired[int]
    fee_type: NotRequired[str]
    currency_code: NotRequired[str]
    pricing_type: NotRequired[str]
    rate_base: NotRequired[float]
    rate_tier1: NotRequired[float]
    rate_tier2: NotRequired[float]
    rate_tier3: NotRequired[float | None]
    rate_tier4: NotRequired[float | None]
    usage_base: NotRequired[float]
    usage_tier1: NotRequired[float]
    usage_tier2: NotRequired[float]
    usage_tier3: NotRequired[float | None]
    usage_tier4: NotRequired[float | None]
    total_base: NotRequired[float]
    total_tier1: NotRequired[float]
    total_tier2: NotRequired[float]
    total_tier3: NotRequired[float]
    total_tier4: NotRequired[float]
    total_due: NotRequired[float]
    net_due: NotRequired[float]
    uom: NotRequired[str]
    is_paid: NotRequired[bool]
    status: NotRequired[str]
