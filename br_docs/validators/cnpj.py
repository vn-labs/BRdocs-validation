import re

from br_docs.validators import CheckTwoDigits


class CNPJv(CheckTwoDigits):
    Patterns = re.compile(r"^\d{14}$"), re.compile(r"^[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}$"),
    CnpjAlgarisms = 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2,

    @classmethod
    def calculate_digits(cls, non_digits: list[int]) -> tuple[int, int]:
        """
            CNPJ's digits checking algorithm.
            https://web.archive.org/web/20240222180515/https://www.macoratti.net/alg_cnpj.htm
        """
        calc = sum(x*y for x, y in zip(non_digits, cls.CnpjAlgarisms[1:])) % 11
        if calc < 2:
            digit_one = 0
        else:
            digit_one = 11 - calc
        non_digits.append(digit_one)
        calc_2 = sum(x*y for x, y in zip(non_digits, cls.CnpjAlgarisms)) % 11
        if calc_2 < 2:
            digit_two = 0
        else:
            digit_two = 11 - calc_2
        return digit_one, digit_two
