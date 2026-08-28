from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class VehicleOption(SdkBaseModel):
    code: Optional[str] = UNSET
    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    color_code: OptionalNullable[str] = Field(default=UNSET, alias="colorCode")
    is_active: Optional[bool] = Field(default=UNSET, alias="isActive")


class VehicleOptionDict(TypedDict):
    code: NotRequired[str]
    display_name: NotRequired[str]
    color_code: NotRequired[str | None]
    is_active: NotRequired[bool]
