import re

from pydantic_core import PydanticCustomError


class ValuesRegex:
    """ Regex for given values """

    Patterns: tuple[re.Pattern, ...]

    def check_format(self, value: str):
        try:
            next(filter(lambda x: x.match(value), self.Patterns))
        except StopIteration:
            raise PydanticCustomError(
                "format",
                "Invalid value's format"
            )
