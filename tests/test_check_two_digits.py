import pytest
from pydantic_core import PydanticCustomError

from br_docs.validators import CheckTwoDigits
from tests import DUMMY_VALUES


@pytest.mark.parametrize('value', DUMMY_VALUES)
def test_validate(value):
    # Arrange
    class Dummy(CheckTwoDigits):

        @staticmethod
        def calculate_digits(non_digits):
            return None, None

    # Assert
    with pytest.raises(PydanticCustomError, match='Invalid value'):
        Dummy().validate(value)
