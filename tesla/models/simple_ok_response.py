from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SimpleOkResponse(SdkBaseModel):
    response: Optional[str] = UNSET


class SimpleOkResponseDict(TypedDict):
    response: NotRequired[str]
