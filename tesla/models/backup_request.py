from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BackupRequest(SdkBaseModel):
    backup_reserve_percent: int


class BackupRequestDict(TypedDict):
    backup_reserve_percent: int
