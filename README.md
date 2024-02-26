![Test](https://github.com/vinicius-oa/BRdocs-validation/actions/workflows/test.yml/badge.svg)
![codecov](https://codecov.io/gh/vinicius-oa/BRdocs-validation/graph/badge.svg?token=Z211YIKO8L)
![PyPI version](https://badge.fury.io/py/brdocs-validation.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/brdocs-validation?color=2334D058)
![Pydantic V2](https://img.shields.io/badge/Pydantic_V2->=2.0-2334D058.svg)

## Install
```
pip install brdocs-validation
```


## Supported docs and its formats

|     Supports      |               Description                |                     Format                      |  Format's support  | 
|:-----------------:|:----------------------------------------:|:-----------------------------------------------:|:------------------:|
|       CNPJ        |                                          | *12.345.678/9012-34* OR _Without special chars_ |                    |
|        CPF        |                                          |   *123.456.789-01* OR _Without special chars_   |                    |
|        CNH        |                                          |                  Only numbers                   |    Length: _11_    |
| NIS/PIS/PASEP/NIT | Use _**NIS**_ type for _PIS, PASEP, NIT_ |       *123.45678.90-1* OR _Only numbers_        |                    |
|        CNS        |         Cartão Nacional de Saúde         |                  Only numbers                   |                    |
|      RENAVAM      |                                          |                  Only numbers                   | Length: _9, 10 & 11_ | 
## Usage 

```python
from br_docs import CNPJ, CPF, CNH, NIS, CNS, RENAVAM
from pydantic import BaseModel


class User(BaseModel):
    cpf: CPF
    cnpj: CNPJ
    cnh: CNH
    nis: NIS
    cns: CNS
    renavam: RENAVAM
```