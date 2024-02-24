import re
from abc import ABC, abstractmethod

from pydantic_core import PydanticCustomError

from br_docs.validators.types.format import ValuesRegex


class CheckTwoDigits(ABC, ValuesRegex):

    def __call__(self, value: str) -> str:
        self.check_format(value)
        self.validate(value)
        return value

    def validate(self, value: str):
        numbers = list(map(int, re.findall(r"\d", value)))
        # Check digits
        digit_one, digit_two = numbers.pop(-2), numbers.pop(-1)
        digit_one_calculated, digit_two_calculated = self.calculate_digits(numbers)
        if digit_one_calculated is not digit_one or digit_two_calculated is not digit_two:
            raise PydanticCustomError(
                'invalid',
                'Invalid value'
            )

    @staticmethod
    @abstractmethod
    def calculate_digits(non_digits):   # pragma: no cover
        ...
