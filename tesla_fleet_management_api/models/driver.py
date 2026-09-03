from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Driver(SdkBaseModel):
    my_tesla_unique_id: Optional[int] = UNSET
    user_id: Optional[int] = UNSET
    user_id_s: Optional[str] = UNSET
    vault_uuid: Optional[str] = UNSET
    driver_first_name: Optional[str] = UNSET
    driver_last_name: Optional[str] = UNSET
    granular_access: Optional[Any] = UNSET
    active_pubkeys: Optional[list[str]] = UNSET
    public_key: Optional[str] = UNSET


class DriverDict(TypedDict):
    my_tesla_unique_id: NotRequired[int]
    user_id: NotRequired[int]
    user_id_s: NotRequired[str]
    vault_uuid: NotRequired[str]
    driver_first_name: NotRequired[str]
    driver_last_name: NotRequired[str]
    granular_access: NotRequired[Any]
    active_pubkeys: NotRequired[list[str]]
    public_key: NotRequired[str]
