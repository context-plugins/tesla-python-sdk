from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WhichTrunk(str, Enum):
    FRONT = "front"
    REAR = "rear"

    __str__ = str.__str__


WhichTrunkOrStr: TypeAlias = Annotated[WhichTrunk | str, open_enum_validator(WhichTrunk)]
