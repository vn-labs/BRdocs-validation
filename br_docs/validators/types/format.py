import re
from abc import ABC

from pydantic_core import PydanticCustomError


class ValuesRegex(ABC):
    """ Regex for given values """

    Patterns: tuple[re.Pattern]

    def check_format(self, value: str):
        if not list(filter(lambda x: x.match(value), self.Patterns)):
            raise PydanticCustomError(
                "format",
                f"Invalid value's format"
            )
