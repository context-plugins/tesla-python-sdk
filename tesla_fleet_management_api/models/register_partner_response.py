from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response_register_partner_response import ResponseRegisterPartnerResponse, ResponseRegisterPartnerResponseDict


class RegisterPartnerResponse(SdkBaseModel):
    response: ResponseRegisterPartnerResponse


class RegisterPartnerResponseDict(TypedDict):
    response: ResponseRegisterPartnerResponse | ResponseRegisterPartnerResponseDict
