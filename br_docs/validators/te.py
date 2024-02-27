import re

from pydantic_core import PydanticCustomError

from br_docs.validators import CheckDigits


class TEv(CheckDigits):
    """ Titulo de eleitor """
    Patterns = re.compile(r"^\d{12}$"),

    def validate(self, value: str):
        valid_value = self.calculate_digits(list(map(int, value)))[0]
        if not valid_value:
            raise PydanticCustomError(
                'invalid',
                'invalid value'
            )

    @staticmethod
    def calculate_digits(value: list[int]) -> tuple[int]:
        """ https://web.archive.org/web/20240226104136/https://exceldoseujeito.com.br/validar-cpf-cnpj-e-titulo-de-eleitor-parte-ii/ """
        check_digit_one = sum(x*y for x, y in zip(value[:8], range(2, 10))) % 11
        if check_digit_one == 10:
            check_digit_one = 0

        value.append(check_digit_one)
        check_digit_two = sum(x*y for x, y in zip(value[8:], range(7, 10))) % 11
        if check_digit_two == 10:
            check_digit_two = 0
        if check_digit_one == value[-3] and check_digit_two == value[-2] and 0 < int(str(value[8]) + str(value[9])) < 29:
            return 1,
        return 0,
