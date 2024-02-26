import re

from br_docs.validators import CheckDigits


class RENAVAMv(CheckDigits):
    Patterns = re.compile(r"^\d{9,11}$"),
    CHECK_DIGITS = 1

    @staticmethod
    def calculate_digits(value: list[int]) -> tuple[int, ...]:
        value_length = len(value)
        if value_length == 8:
            value.insert(0, 0)
            value.insert(0, 0)

        elif value_length == 9:
            value.insert(0, 0)

        value_reversed = value[::-1]
        calc = sum((i + 2) * v for i, v in zip(range(8), value_reversed))
        calc += value_reversed[8] * 2
        calc += value_reversed[9] * 3
        mod11 = calc % 11
        dv = 11 - mod11 if mod11 != 0 else 0
        if dv == 10:
            dv = 0
        return dv,
