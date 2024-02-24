import re

from br_docs.validators import CheckTwoDigits


class CPFv(CheckTwoDigits):
    Patterns = re.compile(r"^(?!(\d)\1{10}$)\d{11}$"), re.compile(r"^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$")

    @staticmethod
    def calculate_digits(non_digits: list[int]) -> tuple[int, int]:
        """ CPF's digits checking algorithm. """
        calc = 11 - (sum((n * (10 - i)) for i, n in enumerate(non_digits)) % 11)
        if calc > 9:
            calc = 0
        non_digits.append(calc)
        calc_2 = 11 - (sum((n * (11 - i)) for i, n in enumerate(non_digits)) % 11)
        if calc_2 > 9:
            calc_2 = 0
        return calc, calc_2
