import re

from pydantic_core import PydanticCustomError


class SEIv:
    Patterns = re.compile(r"^\d{5}-?\d{8}/?\d{4}-?\d{2}$")

    def __call__(self, value: str) -> str:
        self.validate(value)
        return value

    def validate(self, value: str) -> str:
        check_format = bool(self.Patterns.match(value))
        print(check_format)
        if check_format is not True:
            raise PydanticCustomError("invalid", "Invalid Value")
        return value
