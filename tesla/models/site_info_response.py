from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SiteInfoResponse(SdkBaseModel):
    response: Optional[Any] = UNSET


class SiteInfoResponseDict(TypedDict):
    response: NotRequired[Any]
