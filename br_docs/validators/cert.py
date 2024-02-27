import re

from br_docs.validators import CheckDigits


class CERTv(CheckDigits):
    """ Certidões de casamento, nascimento e óbito """
    Patterns = re.compile(r"^\d{32}$"),
    CHECK_DIGITS = 2
    CertAlgarismsMultipliers = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,

    @classmethod
    def calculate_digits(cls, non_digits: list[int]) -> tuple[int, ...]:
        """ https://web.archive.org/web/20240227052915/http://ghiorzi.org/DVnew.htm#zc """
        def sum_(slice_: int = 1, value: int | None = None) -> int:
            numbers = non_digits
            if value is not None:
                numbers.append(value)
            digit = sum(x * y for x, y in zip(numbers, cls.CertAlgarismsMultipliers[slice_:])) % 11
            if digit == 10:
                return 1
            return digit

        digit_one = sum_()
        digit_two = sum_(0, digit_one)
        return digit_one, digit_two
