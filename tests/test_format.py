import re

import pytest
from pydantic_core import PydanticCustomError

from br_docs.validators.types.format import ValuesRegex
from tests import DUMMY_VALUES


@pytest.mark.parametrize('value', DUMMY_VALUES)
def test_check_format(value):
    # Arrange
    class Dummy(ValuesRegex):
        Patterns = re.compile(r"^\d{4}$"),

    # Assert
    with pytest.raises(PydanticCustomError, match='Invalid value\'s format'):
        Dummy().check_format(value)
