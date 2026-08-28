from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProductsResponse(SdkBaseModel):
    response: Optional[list[Any]] = UNSET
    count: Optional[int] = UNSET


class ProductsResponseDict(TypedDict):
    response: NotRequired[list[Any]]
    count: NotRequired[int]
