from contextlib import contextmanager

from pydantic import create_model
from pydantic_core import ValidationError

from br_docs import CNH, CPF, CNPJ


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
