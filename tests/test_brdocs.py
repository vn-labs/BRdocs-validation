from pydantic_core import PydanticCustomError

from br_docs.validators import CPF, CNH


def test_cnh(cnh_list):
    for cnh in cnh_list:
        try:
            CNH()(cnh)
        except PydanticCustomError as exc:
            assert False, f"{exc}: {cnh}"


def test_cpfs(cpf_list):
    for cpf in cpf_list:
        try:
            CPF()(cpf)
        except PydanticCustomError as exc:
            assert False, f"{exc}: {cpf}"
