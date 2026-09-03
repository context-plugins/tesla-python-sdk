from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GuestModeRequest(SdkBaseModel):
    enable: bool
    """Enable or disable Guest Mode"""


class GuestModeRequestDict(TypedDict):
    enable: bool
