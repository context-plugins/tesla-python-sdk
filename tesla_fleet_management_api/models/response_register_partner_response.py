from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ResponseRegisterPartnerResponse(SdkBaseModel):
    client_id: str
    name: str
    description: Optional[str] = UNSET
    domain: str
    ca: OptionalNullable[str] = UNSET
    created_at: RFC3339DateTime
    updated_at: RFC3339DateTime
    enterprise_tier: str
    account_id: str
    issuer: OptionalNullable[str] = UNSET
    csr: OptionalNullable[str] = UNSET
    csr_updated_at: OptionalNullable[RFC3339DateTime] = UNSET
    public_key: str
    public_key_hash: str


class ResponseRegisterPartnerResponseDict(TypedDict):
    client_id: str
    name: str
    description: NotRequired[str]
    domain: str
    ca: NotRequired[str | None]
    created_at: RFC3339DateTime
    updated_at: RFC3339DateTime
    enterprise_tier: str
    account_id: str
    issuer: NotRequired[str | None]
    csr: NotRequired[str | None]
    csr_updated_at: NotRequired[RFC3339DateTime | None]
    public_key: str
    public_key_hash: str
