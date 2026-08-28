from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DefaultRealMode(str, Enum):
    AUTONOMOUS = "autonomous"
    SELF_CONSUMPTION = "self_consumption"

    __str__ = str.__str__


DefaultRealModeOrStr: TypeAlias = Annotated[DefaultRealMode | str, open_enum_validator(DefaultRealMode)]
