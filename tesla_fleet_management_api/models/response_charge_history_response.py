from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .charge_history import ChargeHistory, ChargeHistoryDict


class ResponseChargeHistoryResponse(SdkBaseModel):
    charge_history: list[ChargeHistory]


class ResponseChargeHistoryResponseDict(TypedDict):
    charge_history: list[ChargeHistory | ChargeHistoryDict]
