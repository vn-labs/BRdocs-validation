import re

from pydantic_core import PydanticCustomError

from br_docs.validators import CheckDigits


class CNSv(CheckDigits):
    Patterns = re.compile(r"^\d{15}$"),

    def validate(self, value: str):
        valid_value = self.calculate_digits(list(map(int, value)))[0]
        if not valid_value:
            raise PydanticCustomError(
                'invalid',
                'Invalid value'
            )

    @staticmethod
    def calculate_digits(value: list[int]) -> tuple[int]:
        """ https://web.archive.org/web/20190106003440/http://cartaonet.datasus.gov.br/Rotina_Java.doc """
        def sum_(value_slice=11, range_stop=4):
            return sum(int(x) * y for x, y in zip(value[:value_slice], range(15, range_stop, -1)))

        if value[0] in (1, 2):
            dv = 11 - (sum_() % 11)
            if dv == 11:
                dv = 0
            elif dv == 10:
                dv = 11 - ((sum_() + 2) % 11)
            if dv != value[-1]:
                return 0,
        else:
            dv = sum_(value_slice=len(value), range_stop=0) % 11
            if dv != 0:
                return 0,
        return 1,
