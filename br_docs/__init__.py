from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated

from br_docs.validators.cnh import CNHv
from br_docs.validators.cnpj import CNPJv
from br_docs.validators.cns import CNSv
from br_docs.validators.cpf import CPFv
from br_docs.validators.nis import NISv
from br_docs.validators.renavam import RENAVAMv

CPF = Annotated[str, AfterValidator(CPFv())]
CNPJ = Annotated[str, AfterValidator(CNPJv())]
CNH = Annotated[str, AfterValidator(CNHv())]
NIS = Annotated[str, AfterValidator(NISv())]
CNS = Annotated[str, AfterValidator(CNSv())]
RENAVAM = Annotated[str, AfterValidator(RENAVAMv())]
