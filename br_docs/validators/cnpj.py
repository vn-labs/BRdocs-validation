import re
from math import ceil

from pydantic_core import PydanticCustomError

from br_docs.validators import CheckDigits


class CNPJv(CheckDigits):
    """
    CNPJ validator supporting both numeric (legacy) and alphanumeric (2026+) formats.
    Algorithm: https://www.serpro.gov.br/ (calculodvcnpjalfanaumerico.pdf)
    """

    Patterns = (
        re.compile(r'^\d{14}$'),  # Numeric unformatted
        re.compile(
            r'^[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}$'
        ),  # Numeric formatted
        re.compile(r'^[0-9A-Z]{12}\d{2}$', re.IGNORECASE),  # Alphanumeric unformatted
        re.compile(
            r'^[0-9A-Z]{2}\.[0-9A-Z]{3}\.[0-9A-Z]{3}/[0-9A-Z]{4}-\d{2}$', re.IGNORECASE
        ),  # Alphanumeric formatted
    )
    CHECK_DIGITS = 2
    CnpjAlgarismsMultipliers = 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2

    def validate(self, value: str):
        """Validate CNPJ with alphanumeric support."""
        clean = value.upper().replace('.', '').replace('/', '').replace('-', '')
        base_chars = clean[:-2]
        check_str = clean[-2:]
        try:
            check_1, check_2 = int(check_str[0]), int(check_str[1])
        except ValueError:
            raise PydanticCustomError('invalid', 'Invalid value')
        calc_1, calc_2 = self.calculate_digits_alphanumeric(base_chars)
        if check_1 != calc_1 or check_2 != calc_2:
            raise PydanticCustomError('invalid', 'Invalid value')

    @staticmethod
    def char_to_value(char: str) -> int:
        return ord(char) - 48

    @classmethod
    def calculate_digits_alphanumeric(cls, base_chars: str) -> tuple[int, int]:
        values = [cls.char_to_value(c) for c in base_chars]
        d1 = cls._calc_digit(values)
        d2 = cls._calc_digit(values + [d1])
        return d1, d2

    @staticmethod
    def _calc_digit(values: list[int]) -> int:
        n = len(values)
        weights = []
        for _ in range(ceil(n / 8)):
            weights.extend(range(2, 10))
        weights = weights[:n]
        weights.reverse()
        total = sum(v * w for v, w in zip(values, weights))
        rem = total % 11
        return 0 if rem < 2 else 11 - rem

    @classmethod
    def calculate_digits(cls, non_digits: list[int]) -> tuple[int, int]:
        """Legacy method for backward compatibility."""
        calc = (
            sum(x * y for x, y in zip(non_digits, cls.CnpjAlgarismsMultipliers[1:]))
            % 11
        )
        d1 = 0 if calc < 2 else 11 - calc
        non_digits.append(d1)
        calc2 = (
            sum(x * y for x, y in zip(non_digits, cls.CnpjAlgarismsMultipliers)) % 11
        )
        d2 = 0 if calc2 < 2 else 11 - calc2
        return d1, d2
