import re

from br_docs.validators import CheckDigits


class NISv(CheckDigits):
    """ NIS is the number of NIT, PIS, PASEP and NIS itself. """

    Patterns = re.compile(r"^\d{11}$"), re.compile(r"^[0-9]{3}\.[0-9]{5}\.[0-9]{2}-[0-9]$")
    NisAlgarismsMultipliers = 3, 2, 9, 8, 7, 6, 5, 4, 3, 2
    CHECK_DIGITS = 1

    @classmethod
    def calculate_digits(cls, non_digits: list[int]) -> tuple[int]:
        """ https://web.archive.org/web/20240225202130/https://www.macoratti.net/alg_pis.htm """
        calc = 11 - (sum(x * y for x, y in zip(non_digits, cls.NisAlgarismsMultipliers)) % 11)
        if calc > 9:
            return 0,
        return calc,
