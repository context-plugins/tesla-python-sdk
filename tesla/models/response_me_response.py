from __future__ import annotations

from uuid import UUID

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ResponseMeResponse(SdkBaseModel):
    email: str
    full_name: str
    profile_image_url: str
    vault_uuid: UUID


class ResponseMeResponseDict(TypedDict):
    email: str
    full_name: str
    profile_image_url: str
    vault_uuid: UUID
