from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated

from br_docs.validators import *


CPF = Annotated[str, AfterValidator(CPF())]
CNPJ = Annotated[str, AfterValidator(CNPJ())]
CNH = Annotated[str, AfterValidator(CNH())]
