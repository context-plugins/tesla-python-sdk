from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ChargingInvoice(SdkBaseModel):
    file_name: Optional[str] = Field(default=UNSET, alias="fileName")
    content_id: Optional[str] = Field(default=UNSET, alias="contentId")
    invoice_type: Optional[str] = Field(default=UNSET, alias="invoiceType")


class ChargingInvoiceDict(TypedDict):
    file_name: NotRequired[str]
    content_id: NotRequired[str]
    invoice_type: NotRequired[str]
