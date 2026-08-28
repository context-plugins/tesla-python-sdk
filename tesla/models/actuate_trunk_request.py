from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.which_trunk import WhichTrunkOrStr


class ActuateTrunkRequest(SdkBaseModel):
    which_trunk: WhichTrunkOrStr


class ActuateTrunkRequestDict(TypedDict):
    which_trunk: WhichTrunkOrStr
