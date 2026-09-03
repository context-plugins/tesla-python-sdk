from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .response3 import Response3, Response3Dict


class Api1VehiclesNearbyChargingSitesResponse(SdkBaseModel):
    response: Optional[Response3] = UNSET


class Api1VehiclesNearbyChargingSitesResponseDict(TypedDict):
    response: NotRequired[Response3 | Response3Dict]
