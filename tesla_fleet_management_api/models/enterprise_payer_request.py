from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EnterprisePayerRequest(SdkBaseModel):
    role: str
    federation_id: Optional[str] = UNSET
    account_id: Optional[str] = UNSET


class EnterprisePayerRequestDict(TypedDict):
    role: str
    federation_id: NotRequired[str]
    account_id: NotRequired[str]
