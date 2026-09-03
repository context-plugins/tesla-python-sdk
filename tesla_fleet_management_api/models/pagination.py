from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Pagination(SdkBaseModel):
    previous: OptionalNullable[int] = UNSET
    next: OptionalNullable[int] = UNSET
    current: Optional[int] = UNSET
    per_page: Optional[int] = UNSET
    count: Optional[int] = UNSET
    pages: Optional[int] = UNSET


class PaginationDict(TypedDict):
    previous: NotRequired[int | None]
    next: NotRequired[int | None]
    current: NotRequired[int]
    per_page: NotRequired[int]
    count: NotRequired[int]
    pages: NotRequired[int]
