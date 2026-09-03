from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .response_api1_dx_warranty_details_response import (
    ResponseApi1DxWarrantyDetailsResponse,
    ResponseApi1DxWarrantyDetailsResponseDict,
)


class Api1DxWarrantyDetailsResponse(SdkBaseModel):
    response: Optional[ResponseApi1DxWarrantyDetailsResponse] = UNSET


class Api1DxWarrantyDetailsResponseDict(TypedDict):
    response: NotRequired[ResponseApi1DxWarrantyDetailsResponse | ResponseApi1DxWarrantyDetailsResponseDict]
