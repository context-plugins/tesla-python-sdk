from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class KindGetWallConnectorChargingHistory(str, Enum):
    CHARGE = "charge"

    __str__ = str.__str__


KindGetWallConnectorChargingHistoryOrStr: TypeAlias = Annotated[
    KindGetWallConnectorChargingHistory | str, open_enum_validator(KindGetWallConnectorChargingHistory)
]
