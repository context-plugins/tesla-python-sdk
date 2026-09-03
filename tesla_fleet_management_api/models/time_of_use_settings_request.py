from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .tou_settings import TouSettings, TouSettingsDict


class TimeOfUseSettingsRequest(SdkBaseModel):
    tou_settings: TouSettings


class TimeOfUseSettingsRequestDict(TypedDict):
    tou_settings: TouSettings | TouSettingsDict
