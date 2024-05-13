from contextlib import contextmanager

import pytest
from pydantic import create_model
from pydantic_core import ValidationError

from br_docs import CNH, CPF, CNPJ, NIS, CNS, RENAVAM, TE, CERT, SEI


@contextmanager
def validate(model_name: str, values, value_type):
    try:
        for value in values:
            try:
                m = create_model(model_name, param=(value_type, ...))
                m(param=value)
            except ValidationError as exc:
                raise exc
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


def test_cert(cert_list):
    with validate(model_name='TestCERT', values=cert_list, value_type=CERT):
        pass


def test_valid_sei(valid_sei_list):
    with validate(model_name='TestSEI', values=valid_sei_list, value_type=SEI):
        pass


def test_invalid_sei(invalid_sei_list):
    with pytest.raises(ValidationError):
        with validate(
            model_name='TestSEI',
            values=invalid_sei_list,
            value_type=SEI,
        ):
            pass
