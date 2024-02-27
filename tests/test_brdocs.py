from contextlib import contextmanager

from pydantic import create_model
from pydantic_core import ValidationError

from br_docs import CNH, CPF, CNPJ, NIS, CNS, RENAVAM, TE


@contextmanager
def validate(model_name: str, values, value_type):
    try:
        for value in values:
            try:
                m = create_model(model_name, param=(value_type, ...))
                m(param=value)
            except ValidationError as exc:
                assert False, f"{exc}: {value}"
        yield
    finally:
        pass


def test_cnh(cnh_list):
    with validate(model_name='TestCNH', values=cnh_list, value_type=CNH):
        pass


def test_cpf(cpf_list):
    with validate(model_name='TestCPF', values=cpf_list, value_type=CPF):
        pass


def test_cnpj(cnpj_list):
    with validate(model_name='TestCNPJ', values=cnpj_list, value_type=CNPJ):
        pass


def test_nis(nis_list):
    with validate(model_name='TestNIS', values=nis_list, value_type=NIS):
        pass


def test_cns(cns_list):
    with validate(model_name='TestCNS', values=cns_list, value_type=CNS):
        pass


def test_renavam(renavam_list):
    with validate(model_name='TestRENAVAM', values=renavam_list, value_type=RENAVAM):
        pass


def test_te(te_list):
    with validate(model_name='TestTE', values=te_list, value_type=TE):
        pass
