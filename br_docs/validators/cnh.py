import re

from br_docs.validators import CheckTwoDigits


class CNHv(CheckTwoDigits):
    Patterns = re.compile(r"^\d{11}$"),

    @classmethod
    def calculate_digits(cls, non_digits: list[int]) -> tuple[int, int]:
        """
            CNH's digits checking algorithm.
            https://web.archive.org/web/20240223041941/https://siga0984.wordpress.com/2019/05/01/algoritmos-validacao-de-cnh/
        """
        largest_multipler, smallest_multiplier = 9, 1
        digit_one, digit_two = 0, 0
        is_digit_one_greater_than_nine = False

        for nL in non_digits:
            digit_one += nL * largest_multipler
            digit_two += nL * smallest_multiplier
            largest_multipler -= 1
            smallest_multiplier += 1

        digit_one %= 11
        if digit_one > 9:
            digit_one = 0
            is_digit_one_greater_than_nine = True

        digit_two %= 11
        if is_digit_one_greater_than_nine:
            if digit_two - 2 < 0:
                digit_two += 9
            elif digit_two - 2 >= 0:
                digit_two -= 2

        if digit_two > 9:
            digit_two = 0

        return digit_one, digit_two
