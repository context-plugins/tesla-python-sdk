from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .response_charge_history_response import ResponseChargeHistoryResponse, ResponseChargeHistoryResponseDict


class ChargeHistoryResponse(SdkBaseModel):
    response: ResponseChargeHistoryResponse


class ChargeHistoryResponseDict(TypedDict):
    response: ResponseChargeHistoryResponse | ResponseChargeHistoryResponseDict
