![Test](https://github.com/vinicius-oa/BRdocs-validation/actions/workflows/test.yml/badge.svg)
![codecov](https://codecov.io/gh/vinicius-oa/BRdocs-validation/graph/badge.svg?token=Z211YIKO8L)
![Python 3.6](https://img.shields.io/badge/python-3.9_|_3.10_|_3.11_|_3.12-2334D058.svg)
![Pydantic V2](https://img.shields.io/badge/Pydantic_V2->=2.0-2334D058.svg)

## Install
```
pip install brdocs-validation
```


## Supported docs and its formats

| Supports |                     Format                      |
|:--------:|:-----------------------------------------------:|
|   CNPJ   | *12.345.678/9012-34* OR _Without special chars_ |
|   CPF    |   *123.456.789-01* OR _Without special chars_   |
|   CNH    |                  Only numbers                   |

## Usage 

```python
from br_docs import CPF, CNPJ, CNH
from pydantic import BaseModel


class User(BaseModel): 
    name: str
    age: int
    cpf: CPF
    cnpj: CNPJ
    cnh: CNH
```