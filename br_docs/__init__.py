from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated

from br_docs.validators.cert import CERTv
from br_docs.validators.cnh import CNHv
from br_docs.validators.cnpj import CNPJv
from br_docs.validators.cns import CNSv
from br_docs.validators.cpf import CPFv
from br_docs.validators.nis import NISv
from br_docs.validators.renavam import RENAVAMv
from br_docs.validators.te import TEv


CPF = Annotated[str, AfterValidator(CPFv())]
CNPJ = Annotated[str, AfterValidator(CNPJv())]
CNH = Annotated[str, AfterValidator(CNHv())]
NIS = Annotated[str, AfterValidator(NISv())]
CNS = Annotated[str, AfterValidator(CNSv())]
RENAVAM = Annotated[str, AfterValidator(RENAVAMv())]
TE = Annotated[str, AfterValidator(TEv())]
CERT = Annotated[str, AfterValidator(CERTv())]
