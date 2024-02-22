import re

from br_docs.validators.types.format import ValuesRegex
from br_docs.validators.types.validation import Luhn


class CPF(Luhn, ValuesRegex):
    Patterns = re.compile(r"^\d{11}$"), re.compile(r"^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$"),

    def __call__(self, cpf: str) -> str:
        self.check_format(cpf)
        self.validate(cpf)
        return cpf

    @staticmethod
    def calculate_digits(non_digits: list[int]) -> tuple[int, int]:
        """
            Cálculo dos dois dígitos verificadores de CPF.
            https://web.archive.org/web/20240222143146/http://clubes.obmep.org.br/blog/a-matematica-nos-documentos-a-matematica-dos-cpfs/
        """
        calc = sum(n * (10 - i) for i, n in enumerate(non_digits)) % 11
        if calc < 2:
            digit_one = 0
        else:
            digit_one = 11 - calc
        non_digits.append(digit_one)
        calc_2 = sum(n * (10 - i) for i, n in enumerate(non_digits[1:])) % 11
        if calc_2 < 0:
            digit_two = 0
        else:
            digit_two = 11 - calc_2
        return digit_one, digit_two
