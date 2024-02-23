from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated

from br_docs.validators.cnh import CNHv
from br_docs.validators.cnpj import CNPJv
from br_docs.validators.cpf import CPFv

CPF = Annotated[str, AfterValidator(CPFv())]
CNPJ = Annotated[str, AfterValidator(CNPJv())]
CNH = Annotated[str, AfterValidator(CNHv())]


__all__ = ['CPF', 'CNPJ', 'CNH']
