from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TouSettings(SdkBaseModel):
    tariff_content_v2: Optional[Any] = UNSET


class TouSettingsDict(TypedDict):
    tariff_content_v2: NotRequired[Any]
