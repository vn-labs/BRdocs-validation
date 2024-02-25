import re
from abc import ABC, abstractmethod

from pydantic_core import PydanticCustomError

from br_docs.validators.types.format import ValuesRegex


class CheckDigits(ABC, ValuesRegex):
    CHECK_DIGITS: int
    """ How many check digits does a value has """

    def __call__(self, value: str) -> str:
        self.check_format(value)
        self.validate(value)
        return value

    def validate(self, value: str):
        numbers = list(map(int, re.findall(r"\d", value)))
        check_digits = [numbers.pop(x) for x in range(-self.CHECK_DIGITS, 0)]
        digits_calculated = self.calculate_digits(numbers)
        for check_digit, digit_calculated in zip(check_digits, digits_calculated):
            if check_digit != digit_calculated:
                raise PydanticCustomError(
                    'invalid',
                    'Invalid value'
                )

    @staticmethod
    @abstractmethod
    def calculate_digits(non_digits) -> tuple[int, ...]:   # pragma: no cover
        ...
