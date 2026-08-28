from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .response_api1_dx_vehicles_options_response import (
    ResponseApi1DxVehiclesOptionsResponse,
    ResponseApi1DxVehiclesOptionsResponseDict,
)


class Api1DxVehiclesOptionsResponse(SdkBaseModel):
    response: Optional[ResponseApi1DxVehiclesOptionsResponse] = UNSET


class Api1DxVehiclesOptionsResponseDict(TypedDict):
    response: NotRequired[ResponseApi1DxVehiclesOptionsResponse | ResponseApi1DxVehiclesOptionsResponseDict]
