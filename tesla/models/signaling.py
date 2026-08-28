from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Signaling(SdkBaseModel):
    enabled: bool
    subscribe_connectivity: bool
    use_auth_token: bool


class SignalingDict(TypedDict):
    enabled: bool
    subscribe_connectivity: bool
    use_auth_token: bool
